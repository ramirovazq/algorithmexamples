import numpy as np

np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])

for x in np_height:
    print(x)


print("----------------")

np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])

bmi = np_weight / np_height ** 2

for val in bmi:
    print(val)

print("----------------")
mess = np.array([np_height, np_weight])


for x in mess:
    print(x)


print("----------------")
print(np.nditer(mess))

for val in np.nditer(mess):
    print(val)

