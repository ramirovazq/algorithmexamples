'''
https://www.hackerrank.com/challenges/ctci-fibonacci-numbers/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=recursion-backtracking
'''

# Complete the getMinimumCost function below.
def fibonacci(n): # n number of flowers,  k friends, c list of costs
    list_fibonacci_numbers = [0,1]

    #print("n {} ({})".format(n, n+1))
    for indice, x in enumerate(range(n+1)):

        try:
            list_fibonacci_numbers[indice]
        except IndexError:
            n_1 = list_fibonacci_numbers[indice-1]
            n_2 = list_fibonacci_numbers[indice-2]
            list_fibonacci_numbers.append(n_1+n_2)
        #print("indice {} x {}".format(indice, list_fibonacci_numbers[indice]))

    return list_fibonacci_numbers[n]

if __name__ == '__main__':

    answer = fibonacci(0)
    assert answer == 0, "check code"

    answer = fibonacci(1)
    assert answer == 1, "check code"

    answer = fibonacci(2)
    assert answer == 1, "check code"

    answer = fibonacci(3)
    assert answer == 2, "check code"

    answer = fibonacci(4)
    assert answer == 3, "check code"

    answer = fibonacci(5)
    assert answer == 5, "check code"

    answer = fibonacci(6)
    assert answer == 8, "check code"

    answer = fibonacci(7)
    assert answer == 13, "check code"

    answer = fibonacci(8)
    assert answer == 21, "check code"

    answer = fibonacci(9)
    assert answer == 34, "check code"

    answer = fibonacci(10)
    assert answer == 55, "check code"