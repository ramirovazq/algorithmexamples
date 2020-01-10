
def binary_search(lista, value):
	'''
	lista, must be ordered 
	value, is the number we are searching
	'''
	found = False
	indice = -1 # means not founded

	low = 0 
	high = len(lista) - 1

	while low <= high and not found:
		mid = (low + high) // 2
		#print("low {} ... mid {} ... high {}".format(low, mid, high))
		if lista[mid] == value: 	
			indice = mid
			found = True 
		elif lista[mid] < value: # en lado izquierdo
			#print("lado derecho ....")
			low = mid + 1
		else: # en lado derecho
			#print("lado der ....")
			high = mid - 1
	#while
	return found, indice


if __name__ == '__main__':

	indice = -1
	answer, indice = binary_search([1,2,3,5,8], 8)
	#print("answer ..... indice")
	#print(answer, indice)
	assert True == answer, "check code"

	indice = -1
	answer, indice = binary_search([1,2,3,5,8], 6)
	#print("answer ..... indice")
	#print(answer, indice)
	assert False == answer, "check code"

	indice = -1
	answer, indice = binary_search([1,2,3,5,8], 5)
	#print("answer ..... indice")
	#print(answer, indice)
	assert True == answer, "check code"

	indice = -1
	answer, indice = binary_search([1,2,3,5,8], 2)
	#print("answer ..... indice")
	#print(answer, indice)
	assert True == answer, "check code"