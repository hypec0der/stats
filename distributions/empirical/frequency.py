
import matplotlib.pyplot as plt

#Returns a dictionary with values ​​and their frequencies
def value_counts(data, cumulative=False, normalized=True):

    freq_cumulative = lambda freq_table, i: sum(freq_table[:i])

    unique_data = set(data)

    # Absolute frequencies (counting each value)
    if not normalized: 

        if not cumulative:
        
            return {k: data.count(k) for k in unique_data}

        frequencies = list(value_counts(data, normalized=False).values())

        return {k: freq_cumulative(frequencies, i) for k,i in zip(unique_data, range(len(unique_data)))}

    if not cumulative:
       
        # Frequencies compared to the total
        return {k: data.count(k)/float(len(data)) for k in unique_data}

    frequencies = list(value_counts(data).values())

    return {k: freq_cumulative(frequencies, i) for k,i in zip(unique_data, range(len(unique_data)))}


def freqshape(data, *args, **kwargs):

    values, freqs = (lambda freq_table: (list(freq_table), list(freq_table.values())))(value_counts(data))

    return plt.stem(values, freqs, *args, **kwargs)