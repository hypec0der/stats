
from distributions.empirical.frequency import frqs
import matplotlib.pyplot as plt
from math import log
import numpy as np


def entropy(data, base=2, normalized=True):

    if not normalized: return entropy(data, base, normalized=False) / log(len(data), base)

    return sum(map(lambda f: f*log(1/f, base), frqs(data).values()))


def max_entropy(data, base=2):
    
    return log(len(data), base)


def hshape(data, base=2, *args, **kwargs):

    freqs = sorted(list(frqs(data).values()))

    h_f = [(lambda f: log(1/f, base))(f) for f in freqs]

    plt.plot(freqs, h_f)
