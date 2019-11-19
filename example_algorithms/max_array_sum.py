'''
Sample Input

5 
2 5 8 1 4

Sample Output

11

https://www.hackerrank.com/challenges/max-array-sum/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dynamic-programming

'''


def brutalForecemaxSubsetSum(arr):
    greater_sum = 0
    #print("arr {}".format(arr))
    for index, x in enumerate(arr):
        for y in arr[index+2:]: # two elements combination not adjacent
            #print("x {} y {}".format(x, y))
            if (x + y) > greater_sum:
                greater_sum = x + y
        if len(arr[index::2]) > 2: # three elements combination not adjacent, jumping step size 2
            #print(arr[index::2])
            if sum(arr[index::2]) > greater_sum:
                greater_sum = sum(arr[index::2])
    return greater_sum


def maxSubsetSum(arr):
    print(arr)

    n = len(arr)
    dp = [0 for i in range(n)]

    print("dp {}".format(dp))

    dp[0]=arr[0]
    dp[1]=max(arr[1],arr[0])

    print("dp {}".format(dp))

    print("elementos for ........")
    print(list(range(2,n)))

    for i in range(2,n):

        print("comparing .............. ini")
        print(arr[i])
        print(dp[i-2]+arr[i])
        print(dp[i-1])
        print("comparing .............. fin")

        dp[i]=max(arr[i],dp[i-2]+arr[i],dp[i-1])

        print(dp)
        print("dp ..... changing")
    return(dp[n-1])

if __name__ == "__main__":

    '''
    answer = maxSubsetSum([2,1,5,8,4])
    print(answer)
    assert answer == 11, "check code"


    answer = brutalForecemaxSubsetSum([2,1,5,8,4])
    assert answer == 11, "check code"
    '''

    answer = brutalForecemaxSubsetSum([3,5,-7,8,10])
    print(answer)
    assert answer == 15, "check code"


    '''
    answer = maxSubsetSum([-2,1,3,-4,5])
    print(answer)
    assert answer == 8, "check code"


    answer = maxSubsetSum([3,7,4,6,5])
    print(answer)
    assert answer == 13, "check code"

    answer = maxSubsetSum([3,5,-7,8,10])
    print(answer)
    assert answer == 15, "check code"
    '''