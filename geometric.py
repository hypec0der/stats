
from discrete_variable import DiscreteVariable
from random_variable import RandomVariable as RV
from naturals import Naturals as N
import numpy as np
import math

class Geometric(DiscreteVariable):

    def __init__(self, p):
        # Call super class with a list of possible specifications (infinite, numerative specifications)
        super().__init__()
        # Probability parameter p of success of bernoulli event
        self.p = p

    def pmf(self, x: int):
        # P(X = x) = p(1 - p)^x
        return (((1 - self.p) ** x) * self.p) * RV.I(x in N(1,...,np.Inf))

    def cdf(self, x):
        return sum([self.pmf(k) for k in range(math.floor(x) + 1)])

    def ev(self):
        return (1 - self.p) / self.p

    def var(self):
        return (1 - self.p) / (self.p ** 2)

    def devstd(self):
        return self.var() ** 0.5
        
    def fev(self, e):
        # Given E(X), return Geometric with parameter p
        return Geometric(1/(1+e))
        
    def fvar(self, v):
        # Given Var(X), return Geometric with parameter p
        return Geometric((1 + (1 + 4*v)**0.5) / 2*v)
        
    def fdevstd(self, d):
        # Given DevStd(X), return Geometric with parameter p
        return self.fvar(d**2)

    def __str__(self):
        # Print X ~ P(ℷ)
        return f'X ~ G(p={self.p})'
        
    def pmfshape(self, span, *args, **kwargs):
        # Plot mass probability function on a stick graphic
        return super().pmfshape(span, *args, **kwargs)
        
    def cdfshape(self, span, *args, **kwargs):
        # Plot distribution probability function on curved graphic
        return super().cdfshape(span, *args, **kwargs)
        
    def evshape(self, span, *args, **kwargs):
        # Plot expected value on a dashed line
        super().evshape(span, *args, **kwargs)
