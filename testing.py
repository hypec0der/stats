
from distributions.empirical.pivot import mode, quantile
from distributions.empirical.frequency import frqs
from distributions.empirical.leak import var
import distributions.bernoulli as bernoulli
import distributions.binomial as binomial
from random import choices
import numpy as np


array1 = binomial.simdist(p=0.44, n=10, size=10)

print(array1)

print(frqs(array1, cumulative=True))

print(np.quantile(array1, 0.25))

print(quantile(array1, 0.25))
