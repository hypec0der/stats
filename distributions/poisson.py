
from variables.discrete_variable import DiscreteVariable
from variables.random_variable import RandomVariable as RV
from sets.naturals import Naturals as N
from sets.reals import Reals as R
from random import choices
import matplotlib.pyplot as plt
from math import inf, floor, factorial, e as exp


def simdist(y, limit, size=100):
	
	weigths = (lambda dist: [dist.pmf(i) for i in range(0, limit)])(Poisson(y))

	return choices(range(0, limit), weigths, k=size)


class Poisson(DiscreteVariable):

	''' Poisson's distribution is a discrete probability function that feature probability for 
		independent subsequent events in a given time interval, knowing that on average an y number occurs '''
	
	def __init__(self, y: float=None):
		# Call super class with a list of possible specifications (infinite, numerative specifications)
		super().__init__(samplespace=N([0,...,inf]))

		assert y in N([1,...,inf])
		# Lambda parameter referers to events that occur in average 
		self.y = y
			
	def pmf(self, x: int):
		# P(X = k) = (e^(-ℷ) * ℷ^k) / k!
		return (((exp ** (- self.y)) * (self.y ** x)) / factorial(x)) * RV.I(x in self.samplespace)
		
	def cdf(self, x):
		# P(X <= K) = ∑ P(X = k)
		return sum([self.pmf(k) for k in range(floor(x) + 1)])
		
	def ev(self):
		# E(X) = ∑ (k * P(X = k)) = ℷ
	 	return self.y

	def var(self):
		# Var(X) = ℷ
	 	return self.y

	def devstd(self):
		# DevStd(X) = Var(X) ** 0.5
		return self.var() ** 0.5

	def fev(self, e):
        # Given E(X), return Poisson with parameter y
		return Poisson(e)

	def fvar(self, v):
        # Given Var(X), return Poisson with parameter y
		return Poisson(v)

	def fdevstd(self, d):
        # Given DevStd(X), return Poisson with parameter y
		return self.fvar(d**2)
		
	def __add__(self, other: 'Poisson'):
        # Given X,Y independent => X + Y ~ P(y1 + y2)
		return Poisson(self.y + other.y)

	def __sub__(self, other: 'Poisson'):
        # Given X,Y independent => X - Y ~ P(y1 - y2)
		return Poisson(self.y - other.y)

	def __str__(self):
		# Print X ~ P(ℷ)
		return f'X ~ P(ℷ={self.y})'
	 
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
		pass
