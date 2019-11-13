'''
url https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms
Sample Input 1

10
-59 -36 -13 1 -53 -92 -2 -96 -54 75

Sample Output 1

1
'''


def minimumAbsoluteDifference(arr):
    arr.sort() # sorting the array, we dont need to taste all possible combinations
    list_differences = [] # here we gonna save the absolute differences
    if len(arr) > 0: # array must have at least one element
        first_element = arr[0]
        for x in arr[1:]:
            the_difference = abs(first_element - x)
            list_differences.append(the_difference)
            first_element = x
        list_differences.sort() # smallest difference will be at the beginning
        if len(list_differences) >= 1:
            return list_differences[0]
        return False
    else:
        return False
