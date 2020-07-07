
from random_variable import RandomVariable
from abc import abstractmethod
import matplotlib.pyplot as plt
import numpy as np
import math

class DiscreteVariable(RandomVariable):
	
	def __init__(self):
		super().__init__()
	
	@abstractmethod
	def pmf(self, x):
		pass
	
	@staticmethod
	def fpmf(self, x, c):
		pass

	@staticmethod
	def InvPmf(model, params, x, c):
		return model(*params).fpmf(x,c)

	def pmfshape(self, span, *args, **kwargs):
		# Plot mass probability function on a stick graphic
		return plt.stem(span, [self.pmf(i) for i in span], use_line_collection=True, *args, **kwargs)
		



