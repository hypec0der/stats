

from variables.random_variable import RandomVariable as RV
from variables.continue_variable import ContinueVariable
from sets.reals import Reals as R
from random import expovariate
from math import inf, e as exp


def simdist(y, size=100):

    assert y in R([0,1])
    # Return n random values, 1 with probability p and 0 with probability 1-p
    return [expovariate(y) for i in range(size)]


class Exponential(ContinueVariable):

    def __init__(self, y: float):

        super().__init__(samplespace=R((0,inf)))

        assert y in R((0,1)), Exception

        self.y = y


    def pdf(self, x):
        return (self.y * (exp ** (-self.y * x))) * RV.I(x in self.samplespace)

    def cdf(self, x):
        return (1 - (exp ** (-self.y * x))) * RV.I(x in self.samplespace)

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

    def simulate(self, size=100):
        return [expovariate(self.y) for i in range(size)]