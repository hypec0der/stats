
from random_variable import RandomVariable as RV
from discrete_variable import DiscreteVariable
from naturals import Naturals as N
from scipy.special import comb
import numpy as np
import math

class HiperGeometric(DiscreteVariable):

    def __init__(self, M: int=None, N: int=None, n: int=None):
		# Call super class with a list of possible specifications
        super().__init__()

        self.M = M

        self.N = N

        self.n = n

    def pmf(self, x):
        # P(X = k) = {(N,k)(M,n-k)} / (M+N,n)
        return (comb(self.N,x) * comb(self.M, self.n-x)) / comb(self.M+self.N, self.n) * RV.I(x in N(0,...,self.n))

    def cdf(self, x):
        return sum([self.pmf(k) for k in range(math.floor(x) + 1)])

    def ev(self):
        return (self.N / (self.N+self.M)) * self.n

    def var(self):
        return self.n * (self.N / (self.N+self.M)) * (1 - (self.N / (self.N+self.M))) * (1 - ((self.n-1) / (self.N+self.M-1)))

    def devstd(self):
        return self.var() ** 0.5

    def __str__(self):
        return f'X ~ I(M={self.M}, N={self.N}, n={self.n})'

    def pmfshape(self, span, *args, **kwargs):
        # Plot mass probability function on a stick graphic
        return super().pmfshape(span, *args, **kwargs)
	
    def cdfshape(self, span, *args, **kwargs):
        # Plot distribution probability function on curved graphic
        return super().cdfshape(span, *args, **kwargs)

    def evshape(self, span, *args, **kwargs):
        # Plot expected value on a dashed line
        super().evshape(span, *args, **kwargs)
