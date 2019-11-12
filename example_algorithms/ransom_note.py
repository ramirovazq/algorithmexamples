'''
Sample Input 0

6 4
give me one grand today night
give one grand today

Sample Output 0

Yes

https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
'''

def checkMagazine(magazine, note):
    answer = "No"

    dictionary_magazine = {}
    for x in magazine:
        if x in dictionary_magazine.keys():
            dictionary_magazine[x] += 1
        else:
            dictionary_magazine[x] = 1
    
    for word_in_note in note:
        if word_in_note in dictionary_magazine.keys():
            if dictionary_magazine[word_in_note] > 0:
                dictionary_magazine[word_in_note] -= 1
                answer = "Yes"
            else:
                answer = "No"
                break
        else: # if does not exist a word in the note within magazine, break and answer No
            answer = "No"
            break    
    return answer

if __name__ == "__main__":

    magazine = "give me one grand today night".split()
    note = "give one grand today".split()

    answer = checkMagazine(magazine, note)
    assert answer == "Yes", "sth wrong in the code"
