'''
QUICK SORT PSEUDOCODE
quicksort(A)
    quicksort(A, 0, len(A)-1)
quicksort(A, lo, hi)
    if (lo >= hi) return 
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
import random
def partition(A):
    C     = []
    left  = []
    right = []

    if len(A) > 0:
        pivot_index = random.randint(0,len(A)-1)
        C = ["*"] * len(A)
        pivot = A.pop(pivot_index)
        #print("... PIVOT {}".format(pivot))
        for k in A:
            if k <= pivot:
                left.append(k)
            else:
                right.append(k)
        C = left + [pivot] + right
    return len(left), C

def quicksort_(A):
    if len(A) <= 1:
        #print("condicion base ...{}".format(A))
        return A
    pivot_location, A = partition(A)
    left = quicksort_(A[:pivot_location])
    right = quicksort_(A[pivot_location:])
    return left + right

def quicksort(A=[12,11,13,5,6,7,1,9,8,15]): # son 10 elementos
    return quicksort_(A)

if __name__ == "__main__":
    # partition, working
    print("------------------------------------------------------------")
    print("------------------------PARTITION---------------------------")
    
    z = [12,11,13,5,6,7,1,9,8,15]
    index_pivot, z = partition(z)
    print("index_pivot: {} and z .... {}".format(index_pivot,z))

    index_pivot, z = partition([5,1,6])
    print("index_pivot: {} and z .... {}".format(index_pivot,z))

    index_pivot, z = partition([5,1])
    print("index_pivot: {} and z .... {}".format(index_pivot,z))

    index_pivot, z = partition([5])
    print("index_pivot: {} and z .... {}".format(index_pivot,z))

    index_pivot, z = partition([])
    print("index_pivot: {} and z .... {}".format(index_pivot,z))

    print("-------------------------ENDPARTITION------------------------")
    print("-------------------------------------------------------------")
    
    z = [2,8,7,4,1,0,9,5,3]
    print("original ...................... z")
    print(z)
    answer_a = quicksort(z)
    print("quicksort ...................... answer")
    print(answer_a)

    z = [12,11,13,5,6,7,1,9,8,15]
    print("original ...................... z")
    print(z)
    answer_a = quicksort(z)
    print("quicksort ...................... answer")
    print(answer_a)

    print("compare with ordered ...................... answer ..............................")
    print(answer_a == [1, 5, 6, 7, 8, 9, 11, 12, 13, 15])
