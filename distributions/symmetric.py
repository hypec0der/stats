
from continue_variable import ContinueVariable
from random_variable import RandomVariable as RV
import numpy as np

class Symmetric(ContinueVariable):

    def __init__(self, a, b):

        super().__init__((a,b))

        self.a = a

        self.b = b


    def pdf(self, x):
        # P(a <= X <= n) = 1 / (n-a)
        return 1 / (self.b - self.a) * RV.I(x, space=[self.specs, ])

    def cdf(self, x):
        # P(X <= K) = (K - a) / (n - a)
        return (x - self.a) / (self.b - self.a) * RV.I(x, [self.specs, ]) + RV.I(x, [{self.b}, (self.b, np.Inf)])

    def ev(self):
        # E(X) = (a + b) / 2
        return (self.a + self.b) / 2

    def var(self):
        # Var(X) = (b - a)^2 / 12
        return ((self.b - self.a) ** 2) / 12

    def __str__(self):
        return super().__str__()
        
    def pdfshape(self, x, span=lambda x: np.arange(0,x,0.01)):
        # Plot mass probability function on a stick graphic
        return super().pdfshape(x, span)
        
    def cdfshape(self, x, span=lambda x: np.arange(0,x,0.01)):
        # Plot distribution probability function on curved graphic
        return super().cdfshape(x, span)
