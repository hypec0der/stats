
from numpy import inf, linspace
import math


class Naturals():

    # Function that check if some value is natural value without decimals points and is non-negative
    isNatural = lambda x: (lambda f,d: d >= 0 and f == 0)(*math.modf(x))
    

    def __init__(self, span=[0,...,inf], separator=...):   

        assert span is not None, Exception

        # Check if all values passed as parameters are naturals
        assert all([val is not None and Naturals.isNatural(val) for val in set(span) - {..., inf}]), Exception
        
        self.span = span


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
        # If inf in naturals, then return infinite as count
        if inf in iter(self): return inf
        # Count all specification in range between a ... b
        elif self & {...}: return len((lambda a,b: range(a,b))(*Naturals.get_span(self.span)))
        # Count every single value
        else: return len(self.span)


    def __iter__(self):
        # Return iterator over all values        
        return iter(self.span)