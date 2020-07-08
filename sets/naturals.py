
from orderedset import OrderedSet
from numpy import inf, linspace
import math


class Naturals():

    def __init__(self, span=[0,...,inf]):        
        # Function that check if some value is natural value without decimals points and is non-negative
        isNatural = lambda x: (lambda f,d: d >= 0 and f == 0)(*math.modf(x))
        # Check if all values passed as parameters are naturals
        assert all([val is not None and isNatural(val) for val in set(span) - {..., inf}]), Exception
        #
        self.span = span

    # & does not work properly with ... in OrderedList so override class' method
    def __and__(self, other):
        # Return set intersection between self.set and other.set
        return set(self.span) & other

    @staticmethod
    def get_span(span, separator=...):
        # Return the ends of the range 
        return (lambda i: [span[i-1], span[i+1]])(span.index(separator))

    def __contains__(self, item):
        # There aren't None values in this set
        if item is None: return False
        # Item is sparse in set
        if item in iter(self): return True
        # Item is between some ends separated with ...
        elif self & {...}: return (lambda a,b: item >= a and item <= b)(*Naturals.get_span(self.span))  
        # Item not in set
        return False         

    def __len__(self):
        if inf in iter(self): return inf
        elif self & {...}: return len((lambda a,b: range(a,b))(*Naturals.get_span(self.span)))
        else: return len(self.span)

    def __iter__(self):
        return iter(self.span)