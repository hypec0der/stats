

from variables.random_variable import RandomVariable as RV
from variables.continue_variable import ContinueVariable
from sets.reals import Reals as R
from scipy import integrate
from math import inf, pi, e
from random import gauss


def simdist(mu=0, sigma=1, size=100):
    return [gauss(mu, sigma) for i in range(size)]


class Gaussian(ContinueVariable):

    def __init__(self, mu, sigma):

        super().__init__(samplespace=R((-inf, inf)))
        # Mean
        self.mu = mu
        # teta ∈ R+
        assert sigma >= 0, Exception()
        # Standard deviation
        self.sigma = sigma

    def pdf(self, x, normalized=False):
        return (1/((2*pi)**0.5)) * 1/self.sigma * (e ** ((-1/2) * ((x - self.mu)/self.sigma) ** 2))

    def cdf(self, x):
        return integrate.quad(Gaussian.normal().pdf, -inf, (x - self.mu) / self.sigma)

    def ev(self):
        return self.mu

    def var(self):
        return self.sigma ** 2

    def devstd(self):
        return self.sigma

    @staticmethod
    def normal():
        return Gaussian(0,1)

    def isnorm(self):
        return True if self.mu == 0 and self.sigma == 1 else False
        
    def pdfshape(self, span, *args, **kwargs):
        # Plot mass probability function on a stick graphic
        return super().pdfshape(span, *args, **kwargs)
        
    def cdfshape(self, span, *args, **kwargs):
        # Plot distribution probability function on curved graphic
        return super().cdfshape(span, *args, **kwargs)

    def evshape(self, span, *args, **kwargs):
        # Plot expected value on a dashed line
        super().evshape(span, *args, **kwargs)

    def __add__(self, other):

        assert isinstance(other, (float, int, Gaussian)), Exception

        if isinstance(other, Gaussian):
            # X ~ G(u1,o1), Y ~ G(u2,o2) => (X+Y)~G(u1+u2,o1+o2)
            return Gaussian(self.mu + other.mu, self.sigma + other.teta)
        # X ~ G(u,o), b ∈ R => (X+b)~G(u+b,o)
        return Gaussian(self.mu + other, self.sigma)

    def __mul__(self, a):

        assert isinstance(a, (float, int)), Exception
        # X ~ G(u,o), a ∈ R => (aX)~G(a*u,|a|o)
        return Gaussian(a * self.mu, abs(a) * self.sigma)

    def simulate(self, size=100):
        return [gauss(self.mu, self.sigma) for i in range(size)]