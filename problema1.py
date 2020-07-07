
from bernoulli import Bernoulli
from binomial import Binomial
from poisson import Poisson
from geometric import Geometric
from uniform import Uniform
from symmetric import Symmetric
from gaussian import Gaussian
from exponential import Exponential
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.special import comb
from naturals import Naturals
from random_variable import RandomVariable as RV
from discrete_variable import DiscreteVariable as DV

# 1 se produce fiori bianchi, 0 altrimenti
X = Binomial(4, 0.4)