
from random_variable import RandomVariable
import matplotlib.pyplot as plt
from abc import abstractmethod


class ContinueVariable(RandomVariable):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def pdf(self, x):
        pass

    def pdfshape(self, x, span):
        # Plot mass probability function on a stick graphic
        return plt.plot(span(x), [self.pdf(i) for i in span(x)])
