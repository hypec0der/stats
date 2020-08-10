
from variables.random_variable import RandomVariable
import matplotlib.pyplot as plt
from abc import abstractmethod


class ContinueVariable(RandomVariable):

    def __init__(self, samplespace):
        super().__init__(samplespace)

    @abstractmethod
    def pdf(self, x):
        pass
    
    def pdfshape(self, span, *args, **kwargs):
        # Plot mass probability function on a stick graphic
        return plt.plot(span, list(map(self.pdf, span)), *args, **kwargs)
        
    # Plot distribution probability function on curved graphic
    def cdfshape(self, span, *args, **kwargs):
        return plt.plot(span, list(map(self.cdf, span)), *args, **kwargs)
