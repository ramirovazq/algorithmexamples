'''

Sample Input

2
4
5
1 4 5 3 2
4
4
2 2 4 3

Sample Output

1 4
1 2

https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search

'''


def whatFlavors(cost, money):
    values = {}
    for indice, x in enumerate(cost):
        if (money - x) in values.keys():
            primero = values[money-x]
            segundo = indice + 1
            break
        values[x] = indice + 1

    return (primero, segundo)


if __name__ == "__main__":

    a, b = whatFlavors([1,4,5,3,2], 4) 
    assert (a, b) == (1, 4), "check code"