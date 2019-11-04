'''
QUICK SORT PSEUDOCODE
quicksort(A)
    quicksort(A, 0, len(A)-1)

quicksort(A, lo, hi)
    if (hi >= lo) return 
    pivot_location <- partition(A, lo, hi)
    quicksort(A, lo, pivol_location-1)
    quicksort(A, pivol_location+1, hi)

partition(A, lo, hi)
    pivot_index <- random(lo, hi)
    swap(A, pivot_index, hi)
    pivot <- A[hi]
    i <- lo, j <- hi, C <- new array
    for k = lo to hi - 1:
        if A[k] <= pivot:
            if A[k] <= pivot:
                C[i++] <- A[k]
            else:
                C[j--] <- A[k]
            k++
        C[i] <- A[hi] (copy the pivot in)
        copy C[lo:hi] back into A
        return i

    
    
'''
from merge import merge, mergethree

def quicksort_(A):
    return []

def quicksort(A=[12,11,13,5,6,7,1,9,8,15]): # son 10 elementos
    return quicksort_(A)



if __name__ == "__main__":
    z = [12,11,13,5,6,7,1,9,8,15]

    answer_a = quicksort(z)
    print("quicksort ...................... answer")
    print(answer_a)

    print("compare with ordered ...................... answer ..............................")
    print(answer_a == [1, 5, 6, 7, 8, 9, 11, 12, 13, 15])
