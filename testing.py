
from distributions.empirical.pivot import mode, quantile, mean, qqplot
from distributions.empirical.frequency import frqs
from distributions.empirical.leak import var, distboxplot
import distributions.bernoulli as bernoulli
import distributions.binomial as binomial
import matplotlib.pyplot as plt
from random import choices
import numpy as np

array1 = binomial.simdist(p=0.15, n=10, size=12)

array2 = binomial.simdist(p=0.40, n=10, size=12)

print(sorted(array1))

distboxplot(array1)

plt.show()