
from variables.discrete_variable import DiscreteVariable
from variables.random_variable import RandomVariable as RV
from numpy import inf, arange, linspace
from sets.naturals import Naturals as N
from sets.reals import Reals as R
from random import choices
from math import floor, inf

class Geometric(DiscreteVariable):

    ''' 
    
        The geometric distribution gives the probability that the first occurrence 
        of success requires k independent trials, each with success probability p 
        
        The geometric distribution is an appropriate model if the following assumptions are true:
           - The phenomenon being modeled is a sequence of independent trials.
           - There are only two possible outcomes for each trial, often designated success or failure.
           - The probability of success, p, is the same for every trial.

        If these conditions are true, then the geometric random variable Y 
        is the count of the number of failures before the first success.

        X ~ G(p)    0 <= p <= 1

    '''

    def __init__(self, p):
        # Call super class with a list of possible specifications (infinite, numerative specifications)
        super().__init__(samplespace=N())

        assert p in R([0,1]), Exception
        # Probability parameter p of success of bernoulli event
        self.p = p

    def pmf(self, x: int) -> int:
        # P(X = x) = p(1 - p)^x
        return (((1 - self.p) ** x) * self.p) * RV.I(x in self.samplespace)

    def cdf(self, x: int) -> int:
        return sum([self.pmf(k) for k in range(floor(x) + 1)])

    def ev(self) -> float:
        return (1 - self.p) / self.p

    def var(self) -> float:
        return (1 - self.p) / (self.p ** 2)

    def devstd(self) -> float:
        return self.var() ** 0.5
        
    def __fev(self, e: float) -> 'Geometric':
        # Given E(X), return Geometric with parameter p
        return Geometric(1/(1+e))
        
    def __fvar(self, v: float) -> 'Geometric':
        # Given Var(X), return Geometric with parameter p
        return Geometric((1 + (1 + 4*v)**0.5) / 2*v)
        
    def __fdevstd(self, d: float) -> 'Geometric':
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




        

    
