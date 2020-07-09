

from variables.random_variable import RandomVariable as RV
from variables.continue_variable import ContinueVariable
from sets.reals import Reals as R
from scipy import integrate
from math import inf


class Gaussian(ContinueVariable):

    def __init__(self, mu, teta):

        super().__init__(samplespace=R((np.NINF, np.Inf)))
        # Mean
        self.mu = mu
        # teta ∈ R+
        assert teta >= 0, Exception()
        # Standard deviation
        self.teta = teta

    def pdf(self, x):
        return (1/((2*np.pi)**0.5)) * 1/self.teta * (np.e ** ((-1/2) * ((x - self.mu)/self.teta) ** 2))

    def cdf(self, x):
        return integrate.quad(Gaussian.toNormal().pdf, -inf, (x - self.mu) / self.teta)

    def ev(self):
        return self.mu

    def var(self):
        return self.teta ** 2

    def devstd(self):
        return self.teta

    @staticmethod
    def tonorm():
        return Gaussian(0,1)

    def isnorm(self):
        return True if self.mu == 0 and self.teta == 1 else False

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
        if isinstance(other, Gaussian):
            # X ~ G(u1,o1), Y ~ G(u2,o2) => (X+Y)~G(u1+u2,o1+o2)
            return Gaussian(self.mu + other.mu, self.teta + other.teta)
        # X ~ G(u,o), b ∈ R => (X+b)~G(u+b,o)
        return Gaussian(self.mu + other, self.teta)

    def __mul__(self, a):
        # X ~ G(u,o), a ∈ R => (aX)~G(a*u,|a|o)
        return Gaussian(a * self.mu, abs(a) * self.teta)