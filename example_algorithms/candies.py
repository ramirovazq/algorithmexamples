'''

Sample Input

10
2
4
2
6
1
7
8
9
2
1

Sample Output

19

https://www.hackerrank.com/challenges/candies/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dynamic-programming

'''


def candies(n, arr):
    count = [1]
    # from left to right, we are gonna traverse, adding 1 when x > beforme_element
    for i,x in enumerate(arr[1:],1): # start from element index 1
        if x <= arr[i-1]:
            count.append(1)
        else:
            count.append(count[i-1]+1)
    # now, we are gonna traver grom right to left
    for i,x in enumerate(arr[-2::-1],2):
        if x <= arr[n-i+1]:
            count[n-i] = max(count[n-i], 1)
        else:
            count[n-i] = max(count[n-i], count[n-i+1]+1)
    return sum(count)

if __name__ == '__main__':

    answer = candies(10,[2,4,2,6,1,7,8,9,2,1])
    assert answer == 19, "check your code"

