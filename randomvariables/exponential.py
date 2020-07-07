

from random_variable import RandomVariable as RV
from continue_variable import ContinueVariable
import numpy as np


class Exponential(ContinueVariable):

    def __init__(self, y):

        super().__init__([(0, np.Inf), {0}])

        self.y = y

    def pdf(self, x):
        return (self.y * (np.e ** (-self.y * x))) * RV.I(x, self.specs)

    def cdf(self, x):
        return (1 - (np.e ** (-self.y * x))) * RV.I(x, [self.specs, ])

    def ev(self):
        return 1 / self.y

    def var(self):
        return 1 / (self.y ** 2)

    def dStd(self):
        return 1 / self.y

    def pdfshape(self, x, span=lambda x: np.arange(0,x,0.01)):
        # Plot mass probability function on a stick graphic
        return super().pdfshape(x, span)
        
    def cdfshape(self, x, span=lambda x: np.arange(0,x,0.01)):
        # Plot distribution probability function on curved graphic
        return super().cdfshape(x, span)
