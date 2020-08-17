
from distributions.empirical.pivot import mean


def var(data, distance=lambda x,p: pow(x-p, 2), pivot=mean):

    assert data is not None, Exception

    return (lambda p: sum([distance(x,p) for x in data]))(pivot(data)) / (len(data) - 1)


def devstd(data, distance=lambda x,p: pow(x-p, 2), pivot=mean):

    return pow(var(data, distance, pivot), 0.5)


def interquartilegap(data):

    pass


