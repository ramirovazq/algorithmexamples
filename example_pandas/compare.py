import pandas as pd
import numpy as np

brics = pd.read_csv('paises.csv', index_col=0)
print("----------------------")
print(brics)


print('        ..... .... ...                ')
print('        .....  []  ...                ')
print('        .....  ... ...                ')


print("----------- specific column ['area'] > 8-----------return object, Pandas Series")
is_huge = brics['area'] > 8
print(brics[is_huge])


print("----------- specific column ['area'] > 8-----------return object, Pandas Series")
area_between= np.logical_and(brics['area'] > 8, brics['area'] < 10)
print(brics[area_between])
