
import distributions.bernoulli as bernoulli
import distributions.binomial as binomial
import distributions.geometric as geometric
from distributions.uniform import Uniform
from statsmodels.graphics.gofplots import qqplot_2samples
import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np
from numpy import mean
import scipy.stats
from distributions.exponential import Exponential



X = Exponential(0.3)

print(X.simulate())