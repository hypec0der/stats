
import matplotlib.pyplot as plt
from abc import abstractmethod
import numpy as np
import math

class RandomVariable():
		
	def __init__(self):
		pass

	@abstractmethod
	def cdf(self, x):
		pass
		
	@abstractmethod
	def ev(self):
		pass
		
	@abstractmethod
	def var(self):
		pass
		
	@abstractmethod
	def devstd(self):
		pass

	@abstractmethod
	def simulate(self, *args):
		pass
	
	# Plot distribution probability function on curved graphic
	def cdfshape(self, x, *args, **kwargs):
		return plt.plot(x, list(map(self.cdf, x)), *args, **kwargs)
	
	# Plot distribution probability function on curved graphic
	def evshape(self, x, *args, **kwargs):
		return plt.plot(x, [self.ev() for i in x], *args, **kwargs)

	@staticmethod
	def I(boolean):
		return 1 if boolean is True else 0

	@staticmethod
	def qqplot(data1, data2):
		pass

