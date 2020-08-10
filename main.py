
from distributions.gaussian import Gaussian
import matplotlib.pyplot as plt
from distributions.bernoulli import *
from distributions.binomial import *
from distributions.empirical.mean import mean
import numpy as np

X = Binomial(20, 0.2)

print(X.ev())

bin_sim = simdist(p=0.2, n=20, size=150)

print(mean(bin_sim))

plt.hist(bin_sim, bins=range(0,21))

plt.show()