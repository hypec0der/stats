
from variables.random_variable import RandomVariable as RV
from variables.discrete_variable import DiscreteVariable 
from sets.naturals import Naturals as N
from random import choices
from math import floor

def simdist(specs, size=100):
    return choices(specs, 1/len(specs), k=size)

class Uniform(DiscreteVariable):

    def __init__(self, specs):
        # Call super method with list of specifications (e.g [1,2,3,4,5,6])
        super().__init__(samplespace=N(specs))
        # Number of specifications
        self.n = len(specs)
        
    def pmf(self, x):
        # P(X = k) = 1/n
        return 1 / self.n * RV.I(x in self.samplespace)

    def cdf(self, x):
        #
        return sum([self.pmf(k) for k in range(floor(x) + 1)]) + RV.I(x > self.n)

    def ev(self):
        # E(X) = (n + 1) / 2
        return (self.n + 1) / 2

    def var(self):
        # Var(X) = (n^2 - 1) / 12
        return (self.n**2 - 1) / 12

    def devstd(self):
        return self.var() ** 0.5

    def pmfshape(self, span, *args, **kwargs):
        # Plot mass probability function on a stick graphic
        return super().pmfshape(span, *args, **kwargs)
	
    def cdfshape(self, span, *args, **kwargs):
        # Plot distribution probability function on curved graphic
        return super().cdfshape(span, *args, **kwargs)

    def evshape(self, span, *args, **kwargs):
        # Plot expected value on a dashed line
        super().evshape(span, *args, **kwargs)

    def simulate(self, size=100):
        return choices(self.samplespace, 1/self.n, k=size)