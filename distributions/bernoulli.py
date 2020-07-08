
from variables.discrete_variable import DiscreteVariable
from variables.random_variable import RandomVariable as RV
import distributions.binomial as binomial
from sets.naturals import Naturals as N
from sets.reals import Reals as R
from numpy import linspace, arange, inf
import matplotlib.pyplot as plt
from random import choices
import math


# Return simulation of Bernoulli distribution
def simdist(p, size=100):
    # return 0 with probability 1-p and 1 with probability p for an amount of k times
    return choices([0,1], [1-p, p], k=size)

# Given pmf(x) = P, return new Bernoulli with parameter p
def rvspmf(x: int, P: float):
    # Verify integrity of parameters
    assert x in N([0,...,inf]) and P in R((0,1))
    # p = 
    return Bernoulli(P if x == 0 else 1-P)

# Given E(X), return new Bernoulli with parameter p
def rvsev(P):
    # Excpected value need to be in (0,1)
    assert P in R((0,1)), Exception
    # p = ev
    return Bernoulli(P)

# Given Var(X), return Bernoulli with parameter p
def rvsvar(P):
    # Variance need to be in (0,1)
    assert P in R((0,1)), Exception
    # p = 1 + (1 - (4*var)**0.5)) / 2)
    return Bernoulli((1 + (1-(4*P))**0.5) / 2)

# Given DevStd(X), return Bernoulli with parameter p
def rvsdevstd(P: float) -> 'Bernoulli':
    # Verify integrity of value d passed
    assert P in R((0,1)), Exception
    # p = (1 + (1 - (4*var)**0.5)) / 2)) ** 0.5
    return Bernoulli(rvsvar(P**2))


class Bernoulli(binomial.Binomial):

    ''' 
    
        In probability theory and statistics, the Bernoulli distribution,
        is the discrete probability distribution of a random variable which takes the value 1 with probability p
        and the value 0 with probability q = 1 − p. 
        Less formally, it can be thought of as a model for the set of 
        possible outcomes of any single experiment that asks a yes–no question. 

        X ~ B(p)        0 <= p <= 1

    '''

    def __init__(self, p: float=0):
        # Call super class with a list of possible specifications
        super().__init__(1, p)

    def pmf(self, x: int) -> int:
        # Given X~B(p) then P(X = k) = p if k == 1, 1-p otherwise
        return (self.p if x == 1 else (1-self.p)) * RV.I(x in N(0,1))

    def cdf(self, x: int) -> int:
        # Given X~B(p) then P(X <= K) = ∑ P(X = k)
        return sum([self.pmf(k) for k in range(math.floor(x) + 1)])

    def ev(self) -> float:
        # Given X~B(p) then E(X) = p
        return self.p

    def var(self) -> float:
        # Given X~B(p) then Var(X) = p(1-p)
        return self.p * (1-self.p)

    def devstd(self) -> float:
        # Given X~B(p) then Std(X) = √(Var(X))
        return self.var() ** 0.5

    def __add__(self, other: ('Binomial', 'Bernoulli')) -> 'Binomial':
        # Given X,Y independent => X + Y ~ B(2, p)
        return binomial.Binomial(1 + other.n, self.p)

    def __sub__(self, other: ('Binomial', 'Bernoulli')) -> 'Binomial':       
        # Given X,Y independent => X - Y ~ B(0, p)
        return binomial.Binomial(0, self.p)
    
    def __str__(self):
        # Print X ~ B(p=%d)
        return f'X ~ B(p={self.p})'

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
        # Return simulation of this distribution
        return choices([0,1], [1-self.p, self.p], k=size)
