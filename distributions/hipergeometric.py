
from distributions.random_variable import RandomVariable as RV
from distributions.discrete_variable import DiscreteVariable
from sets.naturals import Naturals as N
from scipy.special import comb
from math import inf

class HiperGeometric(DiscreteVariable):

    def __init__(self, n: int=0, h: int=0, r: int=0):
		# Call super class with a list of possible specifications
        super().__init__(samplespace=N([0,...,n]))

        assert (lambda N: h in N and r in N and n in N)(N([0,...,inf])), Exception
        # h distinct elements of type h, r = n-h elements of another type
        self.h = h; self.r = r
        # Cardinality
        self.n = n

    def pmf(self, x):
        # P(X = k) = {(N,k)(M,n-k)} / (M+N,n)
        return (comb(self.h,x) * comb(self.r, self.n-x)) / comb(self.r+self.h, self.n) * RV.I(x in self.samplespace)

    def cdf(self, x):
        return sum([self.pmf(k) for k in range(math.floor(x) + 1)])

    def ev(self):
        return (self.h / (self.h+self.r)) * self.n

    def var(self):
        return self.n * (self.h / (self.r+self.h)) * (1 - (self.h / (self.r+self.h))) * (1 - ((self.n-1) / (self.r+self.h-1)))

    def devstd(self):
        return self.var() ** 0.5

    def __str__(self):
        return f'X ~ I(n={self.h}, h={self.r}, r={self.n})'

    def pmfshape(self, span, *args, **kwargs):
        # Plot mass probability function on a stick graphic
        return super().pmfshape(span, *args, **kwargs)
	
    def cdfshape(self, span, *args, **kwargs):
        # Plot distribution probability function on curved graphic
        return super().cdfshape(span, *args, **kwargs)

    def evshape(self, span, *args, **kwargs):
        # Plot expected value on a dashed line
        super().evshape(span, *args, **kwargs)
