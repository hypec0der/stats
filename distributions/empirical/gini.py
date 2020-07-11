
from distributions.empirical.frequency import frqs


def I(data, normalized=True):
    
    if normalized: return (I(data, normalized=False)*len(data)) / (len(data) - 1)

    return 1 - sum(map(lambda f: f**2, frqs(data).values()))


def G(data, normalized=True):
    pass