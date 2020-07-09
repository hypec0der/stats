

from variables.random_variable import RandomVariable as RV
from variables.continue_variable import ContinueVariable
from sets.reals import Reals as R
from math import inf


class Exponential(ContinueVariable):

    def __init__(self, y: float):

        super().__init__(samplespace=R((0,inf)))

        assert y in R((0,1)), Exception

        self.y = y


    def pdf(self, x):
        return (self.y * (np.e ** (-self.y * x))) * RV.I(x in self.samplespace)

    def cdf(self, x):
        return (1 - (np.e ** (-self.y * x))) * RV.I(x in self.samplespace)

    def ev(self):
        return 1 / self.y

    def var(self):
        return 1 / (self.y ** 2)

    def devstd(self):
        return 1 / self.y

    def pdfshape(self, span, *args, **kwargs):
        # Plot mass probability function on a stick graphic
        return super().pdfshape(span, *args, **kwargs)
	
    def cdfshape(self, span, *args, **kwargs):
        # Plot distribution probability function on curved graphic
        return super().cdfshape(span, *args, **kwargs)

    def evshape(self, span, *args, **kwargs):
        # Plot expected value on a dashed line
        super().evshape(span, *args, **kwargs)
