
import matplotlib.pyplot as plt
from sets.reals import Reals as R
from math import ceil, floor


# Indice di centralità: restituisce la media aritmetica dei valori contenuti nell'array.
# Stimatore non distorto per il calcolo del valore atteso di una distribuzione
def mean(data: list) -> float:

    assert data is not None, Exception

    return sum(data) / len(data)


# Indice di centralità: restituisce il valore centrale dell'array se dispari, altrimenti la media 
# tra i due valori centrali (n-1/2) + (n/2) / 2
def median(data: list) -> float:

    assert data is not None, Exception

    if len(data) % 2 == 0:

        return (lambda half: sum(data[half-1: half+1]) / 2)(len(data) / 2)

    return data[len(data) / 2]


# Indice di centralità: restituisce il valore che compare più frequentemente nell'array
# Se più valori appaiono con la stessa frequenza, restituisce una tali valori
def mode(data: list) -> list:

    assert data is not None, Exception

    # Raggruppa ciascun elemento con la propria frequenza 
    frequency = {k: data.count(k) for k in set(data)}

    return max(frequency, key=lambda k: frequency[k])


def quantile(data, q):
    
    assert data is not None and q in R((0,1)), Exception

    # Riordino l'array
    data = sorted(data)

    s,e = (ceil(len(data)*q), len(data) - floor(len(data)*(1-q)))

    # Interpolazione
    return (lambda s,e: (s*q + e*(1-q)))(*data[s-1: e+1])


def percentile(data, p):

    return quantile(data, p/100)


def distqqplot(data1, data2, gap=10):

    x = [percentile(data1, i) for i in range(0,100,gap)]

    y = [percentile(data2, i) for i in range(0,100,gap)]

    plt.plot(x,y)