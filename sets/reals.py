
import numpy as np


class Reals(tuple):

    def __init__(self, intll=(np.NINF, np.Inf)): 

        super().__init__()


    def __contains__(self, item):
        # If item is not Real value
        if item is None: return False

        return (lambda a,b: item >= a and item <= b)(*self)


    def __rdiv__(self, item):

        pass
    

    @staticmethod
    def bfzero(f, intll, step=10**(-1), bias=10**(-10)):

        # Generate sequence of numbers included in range (intll) with some step between each number
        v = np.nditer(np.arange(*intll, step))
        # Continue until f(a)*f(b) < 0 (Bolzano's theorem hypothesis)
        while True:
            # Interval (a,b), a < b
            a = next(v, None); b = next(v, None)
            # End of v
            if a is None or b is None:
                # If not found, decrease step to increase sequence of generated numbers
                return Reals.bfzero(f, intll, step=step*10**(-1), bias=bias)

            else:
                # If condition of Bolzano's theorem checked, then
                if f(a)*f(b) < 0:
                    # Call bisection algorithm
                    return Reals.bisection(f, (a,b), bias)


    @staticmethod
    def bisection(f, intll, bias=10**(-10)):
        
        a,b=intll; c=(a+b)/2

        while True:

            if f(c) == 0 or abs(b-c) <= bias: 
                return c

            if f(a)*f(c) > 0: 
                a = c

            else: 
                b = c

            c = (a+b)/2
