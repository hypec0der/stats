
from distributions.empirical.frequency import value_counts
import matplotlib.pyplot as plt
from math import log


def H(data, base=2, normalized=True):

    if not normalized: return H(data, base, normalized=False) / log(len(data), base)

    return sum(map(lambda f: f*log(1/f, base), value_counts(data).values()))
