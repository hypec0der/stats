

from random_variable import RandomVariable as RV
from continue_variable import ContinueVariable
from scipy import integrate
import numpy as np


class Gaussian(ContinueVariable):

    def __init__(self, mu, teta):

        super().__init__((np.NINF, np.Inf))
        # Mean
        self.mu = mu
        # teta ∈ R+
        assert teta >= 0, Exception()
        # Standard deviation
        self.teta = teta

    def pdf(self, x):
        return (1/((2*np.pi)**0.5)) * 1/self.teta * (np.e ** ((-1/2) * ((x - self.mu)/self.teta) ** 2))

    def cdf(self, x):
        return integrate.quad(Gaussian.toNormal().pdf, np.NINF, (x - self.mu) / self.teta)

    def ev(self):
        return self.mu

    def var(self):
        return self.teta ** 2

    def dStd(self):
        return self.teta

    @staticmethod
    def toNormal():
        return Gaussian(0,1)

    def isNormal(self):
        return True if self.mu == 0 and self.teta == 1 else False

    def pdfshape(self, x, span=lambda x: np.arange(0,x,0.01)):
        # Plot mass probability function on a stick graphic
        return super().pdfshape(x, span)
        
    def cdfshape(self, x, span=lambda x: np.arange(0,x,0.01)):
        # Plot distribution probability function on curved graphic
        return super().cdfshape(x, span)

    def __add__(self, other):
        if isinstance(other, Gaussian):
            # X ~ G(u1,o1), Y ~ G(u2,o2) => (X+Y)~G(u1+u2,o1+o2)
            return Gaussian(self.mu + other.mu, self.teta + other.teta)
        # X ~ G(u,o), b ∈ R => (X+b)~G(u+b,o)
        return Gaussian(self.mu + other, self.teta)

    def __mul__(self, a):
        # X ~ G(u,o), a ∈ R => (aX)~G(a*u,|a|o)
        return Gaussian(a * self.mu, abs(a) * self.teta)