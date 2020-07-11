
import matplotlib.pyplot as plt


#Returns a dictionary with values ​​and their frequencies
def frqs(data, cumulative=False, normalized=True):

    # Absolute frequencies (counting each value)
    if not normalized: 

        if cumulative:
        
            freqs = list(frqs(data, normalized=False).values())

            return {k: (lambda i: sum(freqs[:i]))(i) for i,k in enumerate(set(data))}
        
        return {k: data.count(k) for k in set(data)}

    if cumulative:
            
        freqs = list(frqs(data).values())

        return {k: (lambda i: sum(freqs[:i]))(i) for i,k in enumerate(set(data))}

    # Frequencies compared to the total
    return {k: data.count(k)/float(len(data)) for k in set(data)}


def frqstem(data, normalized=True, cumulative=False, *args, **kwargs):

    frequencies = frqs(data, normalized=normalized, cumulative=cumulative)

    return plt.stem(frequencies.keys(), frequencies.values(), use_line_collection=True, *args, **kwargs)

