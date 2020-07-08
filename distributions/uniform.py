
from variables.random_variable import RandomVariable as RV
from variables.discrete_variable import DiscreteVariable 
from sets.naturals import Naturals as N
import numpy as np
import math


class Uniform(DiscreteVariable):

    def __init__(self, n):
        # Call super method with list of specifications (e.g [1,2,3,4,5,6])
        super().__init__()
        
        self.specs = N([0,...,n])

    def pmf(self, x):
        # P(X = k) = 1/n
        return 1 / len(self.specs) * RV.I(x in self.specs)

    def cdf(self, x):
        #
        return sum([self.pmf(k) for k in range(math.floor(x) + 1)]) + RV.I(x > len(self.specs))

    def ev(self):
        # E(X) = (n + 1) / 2
        return (len(self.specs)+1)/2

    def var(self):
        # Var(X) = (n^2 - 1) / 12
        return (len(self.specs)**2 - 1) / 12

    def dStd(self):
        return self.var() ** 0.5

    def pmfshape(self, k, span=lambda k: np.linspace(0,k,endpoint=True,dtype=int)):
        # Plot mass probability function on a stick graphic
        return super().pmfshape(k, span)

    def cdfshape(self, K, span=lambda K: np.arange(0,K,0.01)):
        # Plot distribution probability function on curved graphic
        return super().cdfshape(K, span)
