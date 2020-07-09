
from distributions.empirical.frequency import value_counts


def I(data, normalized=True):
    
    if normalized: return (I(data, normalized=False)*len(data)) / (len(data) - 1)

    return 1 - sum(map(lambda f: f**2, value_counts(data).values()))


def G(data, normalized=True):
    pass