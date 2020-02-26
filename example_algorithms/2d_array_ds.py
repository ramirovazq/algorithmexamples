'''
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
'''
def check3(list_of_elements, indice=0):
	'''
	given a list of elements, 
	check if one element have
	next 2 subsecuent elements
	'''
	answer = False
	try:
		# necessary to exist actual row, and two next rows
		element = list_of_elements[indice] 
		middle_element = list_of_elements[indice+1] 
		last_element   = list_of_elements[indice+2]
		answer = True
	except IndexError:
		pass
	return answer


def hourglassSum(arr):
	print(arr)
	for indice, row in enumerate(arr):
		if check3(arr, indice):
			print(indice, row)
			for indice2, element in enumerate(row):
				if check3(row, indice2):
					print(indice2)
		else:
			break
		


	return 19

if __name__ == '__main__':

	 answer = hourglassSum([[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]])
	 assert answer == 19