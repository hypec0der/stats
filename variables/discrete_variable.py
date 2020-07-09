
from variables.random_variable import RandomVariable
from abc import abstractmethod
import matplotlib.pyplot as plt
import numpy as np
import math


class DiscreteVariable(RandomVariable):
	
	def __init__(self, samplespace):
		super().__init__(samplespace)
	
	@abstractmethod
	def pmf(self, x):
		pass

	def pmfshape(self, span, *args, **kwargs):
		# Plot mass probability function on a stick graphic
		return plt.stem(span, [self.pmf(i) for i in span], use_line_collection=True, *args, **kwargs)
		



