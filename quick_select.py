'''
expectation O(n).  linear .. worst case O(n^2)
QUICK SELECT PSEUDOCODE

quickselect(A, k)
    quickselect(A, 0, len(A)-1, k)

quickselect(A, lo, hi, k)
    if (lo == hi) return A[lo] 
    pivot_location <- partition(A, lo, hi)
    if pivot_location == k
        return A[k]
    else if pivot_location > k:
        return quickselect(A, lo, pivol_location-1, k)
    else:
        quickselect(A, pivol_location+1, hi, k-pivot_location+1)
'''
from quick_sort import partition

def quickselect_(A, k):
    original = A.copy()
    pivot_location, C = partition(A)
    #print("original {} modified {} pivot_location {} .. pivot {} ... finding k {}".format(original, C, pivot_location, C[pivot_location], k))
    if pivot_location == k:
        # exact kth element
        return C[pivot_location]
    elif pivot_location > k:
        # search in left side
        return quickselect_(C[:pivot_location], k)
    else:
        # search in right side
        return quickselect_(C[pivot_location+1:], k - pivot_location - 1)


def quickselect(A=[12,11,13,5,6,7,1,9,8,15], k=6): # son 10 elementos
    return quickselect_(A, k)

if __name__ == "__main__":
         #1,5,6,7,8,9,11,12,13,15
    z = [12,11,13,5,6,7,1,9,8,15]
    answer_a = quickselect(z, 6)
    assert answer_a == 11, ("no encuentra el elemento correcto")

    z = [12,11,13,5,6,7,1,9,8,15]
    answer_a = quickselect(z, 3)
    assert answer_a == 7, ("no encuentra el elemento correcto")
