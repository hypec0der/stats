
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
	def __fev(self, e):
		pass

	@abstractmethod
	def __fvar(self, v):
		pass

	@abstractmethod
	def __fdevstd(self, d):
		pass

	def cdfshape(self, x, *args, **kwargs):
		# Plot distribution probability function on curved graphic
		return plt.plot(x, list(map(self.cdf, x)), *args, **kwargs)

	def evshape(self, x, *args, **kwargs):
		# Plot distribution probability function on curved graphic
		return plt.plot(x, [self.ev() for i in x], *args, **kwargs)

	@staticmethod
	def I(boolean):
		return 1 if boolean is True else 0

	@staticmethod
	def Var(model, params):
		return model(*params).var()

	@staticmethod
	def E(model, params):
		return model(*params).ev()

	@staticmethod
	def DevStd(model, params):
		return model(*params).devstd()

	@staticmethod
	def InvVar(model, params, var):
		return model(*params).fvar(var)

	@staticmethod
	def InvE(model, params, ev):
		return model(*params).fev(ev)

	@staticmethod
	def InvDevStd(model, params, devstd):
		return model(*params).fdevstd(devstd)