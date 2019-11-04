'''
MERGE
merge (A,B)
	C = new array (len(A) + len(B))
	i, j, k <- 0

	while i < len(A) and j < len(B):
		if A[i] < B[j]
			C[k] <- A[i]
			i++, k++
		else
			C[k] <- B[j]
			j++, k++

	while i < len(A):
		C[k++] <- A[i++]
	while j < len(B):
		C[k++] <- B[j++]
	return C

'''
def merge(A=[3,7,12,18], B=[2,5,16,21]):
	'''
	A and B must be already sorted
	'''
	#print("A {}    B {}".format(A,B))
	C = ["*"] * (len(A) + len(B))
	i = j = k = 0
	while i < len(A) and j < len(B):
		if A[i] < B[j]:
			C[k] = A[i]
			i+=1 
			k+=1
		else:
			C[k] = B[j]
			j+=1 
			k+=1
	while i < len(A):
		C[k] = A[i]
		i+=1
		k+=1

	while j < len(B):
		C[k] = B[j]
		j+=1
		k+=1
	return C

def mergethree(A=[3,7,12,18], B=[2,5,16,21], C=[6,8,12,19]):
	'''
	A and B must be already sorted
	'''
	#print("A {}    B {}".format(A,B))
	intermediate = merge(A,B)
	return merge(intermediate, C)


if __name__ == "__main__":
	answer = merge()
	print(answer)

	answer = merge([19],[2])
	print(answer)

	answer = merge([23],[])
	print(answer)

	answer = merge([],[23])
	print(answer)

	answer = merge([],[])
	print(answer)


	answer = merge([1,2,3],[])
	print(answer)

	answer = merge([1,2,3],[1])
	print(answer)

	answer = merge([1,1],[1,2])
	print(answer)


	# Consider merging lists two sorted lists A and B 
	# of length  𝑛  and  𝑚  respectively such that  𝑛<𝑚 , 
	# using the merge function as shown in the lecture slides.

	answer = merge([1,2],[1,2,3,4,5,6,7,8])
	print(answer)

	# In merge sort we decided to split our list into two parts 
	# and recurse on them. 
	# In this question we will consider splitting our list into three parts.