'''
Sample Input

5 4
1 2 3 4 5

Sample Output

5 1 2 3 4

https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
'''

def rotLeft(a, d): #a is the list of elements. d, number of rotations
    '''
    print(a,d)
    print(".....")
    print(d/len(a))
    print(d//len(a))
    print(d % len(a))
    '''
    necessary_rotations = d % len(a)
    #print(necessary_rotations)
    if necessary_rotations == 0: # not necessary rotate
        answer = a
    else:
        answer = a[necessary_rotations:] + a[:necessary_rotations]
    return answer

if __name__ == "__main__":
    list_integers = [1,2,3,4,5]
    answer = rotLeft(list_integers, 4)
    assert answer == [5,1,2,3,4], "rotate had a problem, check cod"
