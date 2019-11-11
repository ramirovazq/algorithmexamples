'''
Sample Input

5
AAAA
BBBBB
ABABABAB
BABABA
AAABBB

Sample Output

3
4
0
0
4

url
https://www.hackerrank.com/challenges/alternating-characters/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
'''


def alternatingCharacters(s):
    #print(s)
    number_deletions = 0
    if len(s) > 0:
        primero = s[0] # first element of array
        #print(primero)
        for x in s[1:]:
            if primero == x:
                number_deletions += 1
            else:
                primero = x
    return number_deletions
