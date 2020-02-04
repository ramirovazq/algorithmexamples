def sockMerchant(n, ar):
    dict_pairs = {}
    pair_number = 0
    for x in ar:
        if x not in dict_pairs.keys():
            dict_pairs[x] = 1
        else: #dict_pairs[x] == 1:
            dict_pairs[x] = dict_pairs[x] + 1
        if dict_pairs[x] == 2:
            pair_number += 1
            del dict_pairs[x]
    return pair_number

if __name__ == '__main__':
    l = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    answer = sockMerchant(len(l), l)
    assert answer == 3, "check your logic"