'''
https://www.hackerrank.com/challenges/ctci-bubble-sort/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting
'''


def swap(a, y, y_next):
    new_a = a.copy()
    value_y = a[y]
    value_y_next = a[y_next]
    new_a[y] = value_y_next
    new_a[y_next] = value_y
    return new_a

# Complete the countSwaps function below.
def countSwaps(a, n): #a list to order, n number of elements
    '''
    for (int i = 0; i < n; i++) {        
        for (int j = 0; j < n - 1; j++) {
            // Swap adjacent elements if they are in decreasing order
            if (a[j] > a[j + 1]) {
                swap(a[j], a[j + 1]);
            }
        }
        
    }
    '''
    swap_counter = 0 
    for x in a:
        #print("element x: {}".format(x))
        for y in range(n-1):
            #print("y {} ... n {}".format(y, list(range(n-1))))
            if (a[y] > a[y+1]):
                swap_counter += 1
                a = swap(a, y, y+1)
    #Array is sorted in 3 swaps.
    #First Element: 1
    #Last Element: 3
    try:
        first_element = a[0]
    except IndexError:
        first_element = None
    try:
        last_element = a[-1]
    except IndexError:
        last_element = None
    return swap_counter, a[0], a[-1]

if __name__ == '__main__':

    counter, first, last = countSwaps([6,4,1], 3)
    assert counter == 3, "check code"
    assert first == 1, "check code"
    assert last == 6, "check code"

    counter, first, last = countSwaps([1,2,3], 3)
    assert counter == 0, "check code"
    assert first == 1, "check code"
    assert last == 3, "check code"

    counter, first, last = countSwaps([3,2,1], 3)
    assert counter == 3, "check code"
    assert first == 1, "check code"
    assert last == 3, "check code"

    counter, first, last = countSwaps([44,43,22,21], 4)
    assert counter == 6, "check code"
    assert first == 21, "check code"
    assert last == 44, "check code"
