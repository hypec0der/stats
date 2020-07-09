
from distributions.empirical import mean
import distributions.bernoulli as bernoulli
import distributions.binomial as binomial
import numpy as np
from distributions.empirical.gini import I
from distributions.empirical.frequency import value_counts, freqshape
from distributions.empirical.entropy import H
import matplotlib.pyplot as plt

data = binomial.simdist(n=100, p=0.5, size=100)

print(value_counts(data, cumulative=True, normalized=True))

plt.show()