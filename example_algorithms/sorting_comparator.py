'''

Sample Input

5
amy 100
ami 100
heraldo 50
aakansha 75
aleksa 150

Sample Output

aleksa 150
ami 100
amy 100
aakansha 75
heraldo 50

https://www.hackerrank.com/challenges/ctci-comparator-sorting/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

'''


from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return [self.name, self.score]

    def __str__(self):
        return "{} {}".format(self.name, self.score)

    def comparator(a, b):
        if a.score > b.score:
            return -1
        elif a.score == b.score: # equal score
            #equal score, means compare by name INI
            if a.name < b.name:
                return -1
            elif a.name == b.name:
                return 0
            elif a.name > b.name:
                return 1
            #equal score, means compare by name FIN
        elif a.score < b.score:
            return 1

    



if __name__ == "__main__":

    n = 5

    data = []
    p = Player("amy", 100)
    data.append(p)

    p = Player("ami", 100)
    data.append(p)

    p = Player("heraldo", 50)
    data.append(p)

    p = Player("aakansha", 75)
    data.append(p)

    p = Player("aleksa", 150)
    data.append(p)

    data = sorted(data, key=cmp_to_key(Player.comparator))
    for i in data:
        print(i.name, i.score)
