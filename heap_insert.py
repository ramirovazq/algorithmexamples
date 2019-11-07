'''
SWIP
swim(A, k):
    while k > 1 and A[k/2] < A[k]:
        swap (A[k], A[k/2])
        k = k / 2

insert(A, k, val)
    N = length(A)
    A[N+1] = val
    swim(A, N+1)
'''
from quick_sort import partition

def swim(k, A): # k es el nodo donde se hizo la inserción
    while (k > 1) and ( A[((k)//2)-1] > A[k-1] ): # if parent is greather than node k
        # swap between node k and his parent
        tmp = A[k-1]                        
        tmp_= A[((k)//2)-1]
        A[((k)//2)-1] = tmp
        A[k-1] = tmp_

        k = k//2
    return A

def insert(val, A=[3,7,6,8,10]): # son 6 elementos
    
    A.append(val) # insert at the final of the list
    N = len(A)
    C = swim(N, A)
    return C

if __name__ == "__main__":

    answer_a = insert(4, [3,7,6,8,10])
    assert answer_a == [3,7,4,8,10,6], ("no encuentra el elemento correcto")

    answer_a = insert(1, [3,7,6,8,10])
    assert answer_a == [1,7,3,8,10,6], ("no encuentra el elemento correcto")

    answer_a = insert(11, [3,7,6,8,10])
    assert answer_a == [3,7,6,8,10,11], ("no encuentra el elemento correcto")
