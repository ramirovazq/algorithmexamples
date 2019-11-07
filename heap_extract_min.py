'''

OPERATION ON HEAPS, Extract Min

sink(A, k):
    N = length(A)
    while 2*k <= N
        smallest = 2*k
        if smallest < N and A[2*k] < A[2*k+ 1]: 
            smallest = 2 * k + 1
        if A[k] < smallest:
            break
        swap (A[k], A[smallest])
        k = smallest


extract-min(A, k)
    N = length(A)
    min = A[1]
    A[1] = A[N]
    sink(A, 1)
    return min
'''
from quick_sort import partition

def sink(A, k):
    N = len(A)
    while (2*k) <= N:
        smallest = (2*k) - 1               # we suppose smallest is left child
        if (A[(2*k)-1] > A[(2*k) + 1 - 1]): # compares, if left child is greater than right child 
            smallest = (2 * k) + 1 - 1      # then right is smallest
        if A[k-1] < A[smallest]:            # if A[k] element is smaller than smallest, we finish
            break

        # swap between smallest and A[k]
        tmp = A[k-1]                        
        tmp_= A[smallest]
        A[smallest] = tmp
        A[k-1] = tmp_

        k = smallest + 1       # we add one cause in heap starts in element 0
        #print("k .... {}".format(k))

    return A

def extract_min(A=[2,3,6,7,10,8]): # son 6 elementos
    N = len(A)
    minimo = A[0]
    A[0] = A[N-1]
    A.pop() # quit last element 
    
    C = sink(A,1)

    assert C == [3,7,6,8,10], ('not final result correct')
    return minimo

if __name__ == "__main__":

    answer_a = extract_min()
    assert answer_a == 2, ("no encuentra el elemento correcto")
