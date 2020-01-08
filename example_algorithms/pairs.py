def pairs(k, arr):
    d = {}
    for y in arr:
        d[y] = y

    count = 0 
    for x in arr:
        number_to_find = x - k
        if number_to_find in d:
            count += 1

    # now we start
    return count

if __name__ == '__main__':

    counter = pairs(2, [1,5,3,4,2])
    assert counter == 3, "check code"