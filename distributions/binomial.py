
from variables.discrete_variable import DiscreteVariable
from variables.random_variable import RandomVariable as RV
import distributions.bernoulli as bernoulli
from numpy import inf, arange, linspace
from sets.naturals import Naturals as N
from sets.reals import Reals as R
import matplotlib.pyplot as plt
from scipy.special import comb
from random import choices
import math


def simdist(p, n, size=100):
    # Generate range of values
    val = linspace(0,n,dtype=int,endpoint=True)
    # Each with same probability of mass function
    probs = (lambda dist: [dist.pmf(i) for i in val])(Binomial(n,p))
    # Return n random values, 1 with probability p and 0 with probability 1-p
    return choices(val, probs, k=size)

def rvspmf(self, x: int, n: int, P: float) -> 'Binomial':
    # Verify integrity of parameters
    assert x in N([0,...,inf]) and n in N([0,...,inf]) and P in R((0,1))
    # The equation to which to apply the zero theorem
    f = lambda c: (comb(n,x) * c**x * (1-c)**(n-x)) - P
    # Given pmf(x) = P, return Binomial with parameter n and p
    return Binomial(n, R.bfzero(f, (0,1)))
        
def rvsev(self,P: float, n: int=None, p: float=None) -> 'Binomial':
    # Almost one parameter need to be defined
    assert (n is not None or p is not None) and P in R((0,1)), Exception
    # Given E(X) and n, return new Binomial with parameter p
    if p is None: return Binomial(n, P/n) 
    # Given E(X) and p, return new Binomial with parameter n
    return Binomial(P/p, p)
        
def rvsvar(self, P: float, n: int=None, p: float=None) -> 'Binomial':
    # Almost one parameter need to be specified
    assert (n is not None or p is not None) and P in R((0,1)), Exception        
    # Given Var(X) and n, return Binomial with parameter p
    if p is None: return Binomial(n, (1 + (1-(4*(P/n)))**0.5) / 2)
    # Given Var(X) and p, return Binomial with parameter n
    return Binomial(P/(p*(1-p)), p)
        
def rvsdevstd(self, P: float):
    # Verify integrity of value d passed
    assert P in R((0,1)), Exception
    # Given DevStd(X), return new Binomial with parameter p or n
    return self.fvar(P**2)


class Binomial(DiscreteVariable):

    '''

        The binomial distribution with parameters n and p is the discrete probability 
        distribution of the number of successes in a sequence of n independent experiments

        The binomial distribution is frequently used to model the number of successes 
        in a sample of size n drawn with replacement from a population of size N

        X ~ B(n,p)      0 <= p <= 1, n € N

    '''

    def __init__(self, n: int=0, p: float=0):
        # Call super class with list of specifications
        super().__init__(samplespace=N([0,...,n]))
        # p need to be in (0,1) and n must be natural value
        assert p in R([0,1]) and n in N()
        # Probability parameter p of success of bernoulli event
        self.p = p 
        # Number of independents events
        self.n = n

    def pmf(self, x: int) -> int:
        # P(X = k) = (n,k) * p^k * (1-p)^(n-k)
        return (comb(self.n, x) * (self.p ** x) * ((1 - self.p) ** (self.n - x))) * RV.I(x in self.samplespace)

    def cdf(self, x: (float, int)) -> int:
        # P(X <= K) = ∑ P(X=k), k ∈ [1,n]
        return sum([self.pmf(k) for k in range(math.floor(x) + 1)]) + RV.I(x > self.n)

    def ev(self) -> float:
        # E(X) = ∑ (k * P(X=k)), k ∈ [1,n] = np
        return self.n * self.p 

    def var(self) -> float:
        # Var(X) = E(X^2) - E(X)^2 = np(1-p)
        return (self.n * self.p) * (1 - self.p)

    def devstd(self) -> float:
        # DevStd(X) = Var(X)
        return self.var() ** 0.5

    def __add__(self, other: ('Binomial', 'Bernoulli')):
        # Given X~B(n,p), Y~(m,p) independents => X + Y ~ B(n+m, p)
        return Binomial(self.n + other.n, self.p)

    def __sub__(self, other: ('Binomial', 'Bernoulli')):
        # Difference of independents Binomial's variable := (X~B(n,p) - Y~B(m,p)) ~ B(n-m, p)
        return Binomial(self.n - other.n, self.p)

    def __str__(self):
        # Print X ~ B(n, p)
        return f'X ~ B(n={self.n}, p={self.p})'

    def __iter__(self):
        # Return binomial distribution as an array of bernoulli independent variable
        return [bernoulli.Bernoulli(self.p) for i in range(self.n)]

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
        # Generate range of values
        val = linspace(0,self.n,dtype=int,endpoint=True)
        # Each with same probability of mass function
        probs = [self.pmf(i) for i in val]
        # Return n random values, 1 with probability p and 0 with probability 1-p
        return choices(val, probs, k=size)

        

    