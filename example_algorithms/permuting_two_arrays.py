'''
Permuting two arrays

Sample Input

2.       # number of queries, two queries in this case
3 10.    # n k  n .. number of elements in array, k the relation variable
2 1 3.   # array A
7 8 9.   # array B
4 5.     # n k  n .. number of elements in array, k the relation variable
1 2 2 1
3 3 3 4
Sample Output

YES
NO

'''


def twoArrays(k, A, B):
    aswer = "NO"
    # first sort A
    A.sort()
    B.sort(reverse=True)

    for indice, x in enumerate(A):
        if x + B[indice] >= k:
            answer = "YES"
        else:
            answer = "NO"
            break
    return answer
