
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


X = binomial.Binomial(10, 0.5)

binomial_tests = binomial.simdist(0.5, 10, size=30)

print(binomial_tests)

print(X.simulate(size=30))