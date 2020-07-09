
from variables.continue_variable import ContinueVariable
from variables.random_variable import RandomVariable as RV
from sets.reals import Reals as R
from math import inf

class Symmetric(ContinueVariable):

    def __init__(self, a, b):
        super().__init__(samplespace=R((a,b)))


    def pdf(self, x):
        # P(a <= X <= n) = 1 / (n-a)
        return 1 / (self.b - self.a) * RV.I(x in self.samplespace)

    def cdf(self, x):
        # P(X <= K) = (K - a) / (n - a)
        return (x - self.a) / (self.b - self.a) * RV.I(x in self.samplespace) + RV.I(x > len(self.samplespace))

    def ev(self):
        # E(X) = (a + b) / 2
        return (self.a + self.b) / 2

    def var(self):
        # Var(X) = (b - a)^2 / 12
        return ((self.b - self.a) ** 2) / 12

    def __str__(self):
        return super().__str__()
        
    def pdfshape(self, span, *args, **kwargs):
        # Plot mass probability function on a stick graphic
        return super().pdfshape(span, *args, **kwargs)
	
    def cdfshape(self, span, *args, **kwargs):
        # Plot distribution probability function on curved graphic
        return super().cdfshape(span, *args, **kwargs)

    def evshape(self, span, *args, **kwargs):
        # Plot expected value on a dashed line
        super().evshape(span, *args, **kwargs)
