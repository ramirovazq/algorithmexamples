def maximumToys(prices, k):
    prices.sort()
    count = 0
    for i in prices:
        #print("count {} .. (i) price {} k {}".format(count, i, k))
        if (i <= k):
            count += 1
            k = k - i
        else:
            break
    return count

def maximumToysR(prices, k):
    prices.sort()
    #print("prices {}, money to spent {}".format(prices, k))
    
    num_toys = 0    
    # it is only one time needed. Why?, cause prices are sorted, so the maxium number of toys, are with cheaper toys,
    # wich appears in the left. If exists other possibiliy in the right, 
    # this posibility will be smaller (in number) than with cheapest toys.
    sum_prices = 0
    for num_times, x in enumerate(prices):
        sum_prices += x
        if sum_prices < k:
            num_toys += 1
            continue
        else:
            break
    return num_toys


if __name__ == "__main__":
    list_prices = [6,4,3,1,2,5]
    answer = maximumToys(list_prices, 4)
    print(answer)

    list_prices = [1,12,5,111,200,1000,10]
    answer = maximumToys(list_prices, 50)
    print(answer)

    list_prices = [6,4,3,1,2,5]
    answer = maximumToysR(list_prices, 4)
    print(answer)

    list_prices = [1,12,5,111,200,1000,10]
    answer = maximumToysR(list_prices, 50)
    print(answer)