import pandas as pd

a = pd.read_csv('paises.csv', index_col=0)
print("----------- a -----------")
print(a)

print("----------- pais  -----------")
pais = a[['pais']]
print(pais)
print(type(pais))

print("----------- unique  -----------")
pais_unique = a['pais'].unique()
print(pais_unique)
print(type(pais_unique))

print("----------- unique  ---- tolist -------")
pais_unique_list = a['pais'].unique().tolist()
print(pais_unique_list)
print(type(pais_unique_list))

print("----------- iter -------")

for x in pais_unique_list:
	print("x {}".format(x))
	index = a['pais'].isin([x])
	print("index ....")
	print(index)
	df = a[index].copy()
	print("df ....")
	print(df)

print("----------- capital -------")
capital = a['capital']
print(capital)
print("----------- shift -------")
capital_shift = a['capital'].shift()
print(capital_shift)
print("----------- shift 2-------")
capital_shift_two = a['capital'].shift(periods=2)
print(capital_shift_two)