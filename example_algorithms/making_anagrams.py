'''

Sample Input

cde
abc

Sample Output

4

https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
'''

def letters_frequency(word=""):
    '''
    retun a dict, 
    key letter and value, 
    frequency appears in word
    example {'a': 1, 'b': 1, 'c': 1}
    '''
    dict_words={}
    for letter in word:
        if not letter in dict_words.keys():
            dict_words[letter] = 1
        else:
            dict_words[letter] = dict_words[letter] + 1
    return dict_words

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    dict_a = letters_frequency(a)
    dict_b = letters_frequency(b)

    number_deletions = 0
    # now, we need to compare both dicts
    for a_letter in dict_a:
        if a_letter in dict_b.keys(): #could be part of anagram
            if dict_a[a_letter] == dict_b[a_letter]: # same letter and same frecuency
                pass # ANAGRAM LETTER
            else:
                number_deletions = number_deletions + abs(dict_a[a_letter] - dict_b[a_letter])
            del dict_b[a_letter]
        else: # appears in dict_a but not in b, so we need to count
            number_deletions = number_deletions + dict_a[a_letter]           

    # now, we need to count letters in dict b, that still exists
    for b_letter in dict_b:
        number_deletions = number_deletions + dict_b[b_letter]
    return number_deletions


if __name__ == "__main__":

    answer = makeAnagram("cde", "abc")
    assert answer == 4, "anagram not working, check cod"
