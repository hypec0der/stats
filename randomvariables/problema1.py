
from geometric import Geometric


X = Geometric(15/20)

print(f'Probabilità di avere 20 estrazioni {X.pmf(20)}')

print(f'Probabilità di avere almeno 10 estrazioni {1 - X.cdf(9)}') 