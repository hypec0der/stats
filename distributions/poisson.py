
from discrete_variable import DiscreteVariable
from random_variable import RandomVariable as RV
from naturals import Naturals as N
from reals import Reals as R
import matplotlib.pyplot as plt
from scipy.special import lambertw
from math import inf


class Poisson(DiscreteVariable):

	''' Poisson's distribution is a discrete probability function that feature probability for 
		independent subsequent events in a given time interval, knowing that on average an y number occurs '''
	
	def __init__(self, y: float=None):
		# Call super class with a list of possible specifications (infinite, numerative specifications)
		super().__init__(samplespace=N([0,...,inf]))

		assert y in R([0,1])
		# Lambda parameter referers to events that occur in average 
		self.y = y
			
	def pmf(self, x: int):
		# P(X = k) = (e^(-ℷ) * ℷ^k) / k!
		return (((math.e ** (- self.y)) * (self.y ** x)) / math.factorial(x)) * RV.I(x in self.samplespace)
		
	def cdf(self, x):
		# P(X <= K) = ∑ P(X = k)
		return sum([self.pmf(k) for k in range(math.floor(x) + 1)])
		
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

