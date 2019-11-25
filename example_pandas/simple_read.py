import pandas as pd

brics = pd.read_csv('paises.csv', index_col=0)
print("----------------------")
print(brics)


print('        ..... .... ...                ')
print('        .....  []  ...                ')
print('        .....  ... ...                ')


print("----------- specific column ['pais']-----------return object, Pandas Series")
print(brics['pais'])
print("----------- specific column [['pais']]-----------, return DataFrame")
print(brics[['pais']])
print("----------- specific columns [['pais', 'capital']]-----------")
print(brics[['pais','capital']])
print("----------- rows [1:4]-----------")
print(brics[1:4])


print('        ..... .... ...                ')
print('        .....  loc ...                ')
print('        .....  ... ...                ')



print("----------- row using loc['RU']----------- return object, Pandas Series")
print(brics.loc['RU'])
print("----------- row using loc[['RU']]-----------")
print(brics.loc[['RU']])
print("----------- row using loc[['RU','IN','SA']]----------- ")
print(brics.loc[['RU','CH','SA']])
print("----------- row using loc[['RU','IN','SA'],['pais', 'capital']]----------- ")
print(brics.loc[['RU','CH','SA'],['pais', 'capital']])
print("----------- row using loc[:,['pais', 'capital']]----------- ")
print(brics.loc[:,['pais', 'capital']])



print('        ..... .... ...                ')
print('        .....  iloc ...                ')
print('        .....  ... ...                ')

print("----------- row using iloc[1]----------- return object, Pandas Series")
print(brics.iloc[[1]])
print("----------- row using iloc[[1,2,3]]----------- ")
print(brics.iloc[[1,2,3]])
print("----------- row using iloc[1:4,:]----------- ")
print(brics.iloc[1:4,:])
