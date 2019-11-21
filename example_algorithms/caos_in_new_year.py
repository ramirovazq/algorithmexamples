'''

Sample Input

2
5
2 1 5 3 4
5
2 5 1 3 4

Sample Output

3
Too chaotic

https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
'''

def minimumBribes(q):
    #print("{}------ case q".format(q))
    # reference list: is the list of integers like if nothing has been moved
    reference_list = list(range(1,len(q)+1))
    reference_list.reverse()
    #print("{} ---- reference list ".format(reference_list))

    number_moves = 0
    for x in reference_list:
        expected_index = x - 1
        #print("x {} expected_index {} q {}".format(x,expected_index,q))
        if x == q[expected_index]: # its in the right place
            q.pop(expected_index)
            pass
        elif x == q[expected_index - 1]: # it has been moved 1 position
            #print("ping1")
            number_moves += 1
            q.pop(expected_index - 1)
        elif x == q[expected_index - 2]: # it has been moved 2 positions
            #print("ping2")
            number_moves += 2
            q.pop(expected_index - 2)
        else:
            return 'Too chaotic'

    return number_moves

if __name__ == "__main__":

    answer = minimumBribes([2, 1, 5, 3, 4])
    assert answer == 3, "check code"

    answer = minimumBribes([2, 5, 1, 3, 4])
    assert answer == 'Too chaotic', "check code"
