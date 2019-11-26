def chunkIt(l, n):
    n = max(1, n)
    return (l[i:i+n] for i in range(0, len(l), n))

# Complete the getMinimumCost function below.
def getMinimumCost(n, k, c): # n number of flowers,  k friends, c list of costs
    
    #print("n flowers {} k friends {}".format(n,k))
    # first we need to order list of costs. Expensive flowers, must be 
    # divided between all posible friends
    c.sort()
    #print("c .....")
    #print(c)
    # im going to complete my array with zeros in left, if it is not exact
    if (n % k) != 0:
        zeros_left = k - (n % k)
        #print("not exact .. zeros left {}".format(zeros_left))
        c = zeros_left * [0] + c
        #print("c {}".format(c))
    #else:
     #   print("exact ......")

    #print("c .....")
    #print(c)

    
    # im creating a list of lists
    c_sliced = list(chunkIt(c, k))
    c_sliced.reverse()

    multiply = 1
    total = 0
    # this is n time, we are traversing entire array
    for sublist in c_sliced:
        for x in sublist:
            total = total + (x * multiply)
        multiply += 1
    return total

if __name__ == '__main__':

    answer = getMinimumCost(55, 34, [433515, 22221, 540709, 538312, 496949, 902471, 439983, 159332, 417327, 399306, 817804, 354682, 108825, 970689, 868286, 235070, 18732, 848955, 994152, 741000, 722232, 564879, 503093, 734475, 174795, 129065, 483929, 683440, 37645, 670198, 911023, 40334, 329513, 669160, 180034, 285512, 401190, 629798, 857703, 765572, 174164, 849299, 159367, 62467, 84449, 523962, 735995, 245666, 832139, 879827, 749840, 315756, 253168, 659252, 187178])
    #print("answer {} ...".format(answer))
    assert answer == 30352414, "check code"