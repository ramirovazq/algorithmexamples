'''
MERGE SORT
mergesort (A)
    mergesort(A, 0, len(A)-1)

mergesort(A, lo, hi)
    if (hi-lo <= 0) return 
    mid = (lo + hi) / 2
    mergesort(A, lo, mid)
    mergesort(A, mid+1, hi)
    C = merge(A[lo:mid], A[mid+1,hi])
    copy elements from C back into A

'''
from merge import merge, mergethree

def mergesort_three(A):
    if len(A) <= 1: # returns the list when is one element
        return A
    mid = len(A) // 3
    if mid == 0: # case when list is 2 elements
        mid = 1
    primera = mergesort_three(A[:mid])
    segunda = mergesort_three(A[mid:mid*2])
    tercera = mergesort_three(A[mid*2:])
    return merge(merge(primera,segunda),tercera)

def mergesortthree(A=[12,11,13,5,6,7,1,9,8,15]): # son 10 elementos
    return mergesort_three(A)

# ............................

def mergesort_(A):
    if len(A) <= 1: # returns the list when is one element
        return A
    mid = len(A) // 2
    primera = mergesort_(A[:mid])
    segunda = mergesort_(A[mid:])
    #print("primera {}  segunda {}".format(primera, segunda))
    return merge(primera, segunda)

def mergesort(A=[12,11,13,5,6,7,1,9,8,15]): # son 10 elementos
    return mergesort_(A)

# second way diveded in two functions
def split(input_list):
    input_list_len = len(input_list)
    midpoint = input_list_len // 2
    return input_list[:midpoint], input_list[midpoint:]

def merge_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    else:
        left, right = split(input_list)
        return merge(merge_sort(left), merge_sort(right))


if __name__ == "__main__":
    z = [12,11,13,5,6,7,1,9,8,15]
    answer_a = mergesort(z)
    print("mergesort ...................... answer")
    print(answer_a)

    answer_b = merge_sort(z)
    print("merge_sort ...................... answer ..............................")
    print(answer_b)

    answer_c = mergesortthree(z)
    print("mergesortthree ...................... answer")
    print(answer_c)

    print("compare tree versiones ...................... answer ..............................")
    print(answer_a == answer_b == answer_c)
