'''
 INSERTION SORT
for i <- 1 to len(A)
	j <- i
	while j > 0 and A[j-1] < A[j]:
		swap A[j] and A[j-1]
		j <- j - 1
'''
def insertion_sort(A=[5,2,4,6,1,3]):
	print("original .......")
	print(A)
	for i, element_i in enumerate(A):
		j = i
		while j > 0 and A[j-1] > A[j]:
			temp = A[j]
			anterior_temp = A[j-1]
			A[j] = anterior_temp
			A[j-1] = temp
			j = j - 1
	return A
A_ordered = insertion_sort()
print("answer insertion sort.......")
print(A_ordered)

print(" ")
print(" ")
print(" ")
'''
 INSERTION SORT QUIZ 1.1
 Given an array A, let’s say that there is an inversion between indices i and j if i < j but A[i] > A[j].
 Inversions can be removed by swapping two elements.
'''
def insertion_sort_quiz(A=[5,2,4,6,1,3]):
	for i, element_i in enumerate(A):
		j = i
		while j > 0 and A[j-1] < A[j]:
			temp = A[j]
			anterior_temp = A[j-1]
			A[j] = anterior_temp
			A[j-1] = temp
			j = j - 1
	return A
A_ordered = insertion_sort_quiz()
print("answer .......quiz")
print(A_ordered)