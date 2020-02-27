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
	answer = [[],[],[]]
	try:
		# necessary to exist actual row, and two next rows
		element = list_of_elements[indice] 
		middle_element = list_of_elements[indice+1] 
		last_element   = list_of_elements[indice+2]
		answer = [element,middle_element,last_element]
	except IndexError:
		pass
	return answer


def hourglassSum(arr):
	print(arr)
	for indice, row in enumerate(arr):
		list_with_lists = check3(arr, indice)
		if any(list_with_lists):
			print("___________ini")
			
			first_list  = list_with_lists[0]
			middle_list = list_with_lists[1]
			last_list   = list_with_lists[2]
			print(".....first_list, middle_list, last_list...")
			print(first_list, middle_list, last_list)

			for indice_element, element in enumerate(first_list):
				group_first  = check3(first_list, indice_element)
				group_middle = check3(middle_list, indice_element)
				group_last   = check3(last_list, indice_element)

				print(".....group_three...ini")
				print(group_first)
				print(group_middle)
				print(group_last)
				print(".....group_three...fin")

			print("___________fin")



		else:
			break
		


	return 19

if __name__ == '__main__':

	 answer = hourglassSum([[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]])
	 assert answer == 19