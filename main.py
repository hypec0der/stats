
import distributions.bernoulli as bernoulli
import distributions.binomial as binomial
from statsmodels.graphics.gofplots import qqplot_2samples
import matplotlib.pyplot as plt
import numpy as np
from numpy import mean
import scipy.stats


tests = scipy.stats.distributions.binom.rvs(p=0.75, n=50, size = 10000)

data = binomial.Binomial.simdist(0.75, n=50, k=10000)

qqplot_2samples(tests, np.array(data))

plt.show()