'''

Sample Input

4 2
1 2 2 4

Sample Output

2

https://www.hackerrank.com/challenges/count-triplets-1/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

'''

# Complete the countTriplets function below.
def counting_frequency(dict_frequency, x):
    if x not in dict_frequency.keys():
        dict_frequency[x] = 1
    else:
        dict_frequency[x] = dict_frequency[x] + 1
    return dict_frequency


def countTriplets(arr, r):
    # will be counting in a dictionary left and right elements of actual element 
    left_frequency  = {}
    right_frequency = {}

    for x in arr:
        right_frequency = counting_frequency(right_frequency, x)

    count = 0
    #iterate over array
    for index, actual_element in enumerate(arr):

        # tiplet means a < a*r < a*r*r
        # in other words a/r < a < a*r

        past_element   =  int(actual_element/r) # a/r
        left = 0
        # actual_element  a
        next_element   =  actual_element * r # a * r
        right = 0

        # quit in right dictionary the actual element
        right_frequency[actual_element] = right_frequency[actual_element] -1

        if (past_element in left_frequency.keys()) and (actual_element % r == 0):
            left = left_frequency[past_element]

        if (next_element in right_frequency.keys()):
            right = right_frequency[next_element]

        count = count + (left * right)

        left_frequency = counting_frequency(left_frequency, actual_element)

    return count

    
if __name__ == "__main__":

    answer = countTriplets([1,3,3,9,9,9,27,81], 3) 
    assert answer == 15, "check code"