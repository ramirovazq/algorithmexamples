def return_median(list_frequencies, index_median, odd=True): # impar True

    index_median_left = index_median - 1 # one before median
    index_median_ok = index_median
    #print("antes del for ...median_left {} median_ok {}".format(index_median_left, index_median_ok))

    must_continue = True
    for indice, x in enumerate(list_frequencies):
        if must_continue:
            index_median_left = index_median_left - x 
        index_median_ok = index_median_ok - x 
        #print("..... ..... {} {} ".format(index_median_left, index_median_ok))
        if index_median_left <= 0 and must_continue:
            #print("entraaaa ++++")
            index_median_left = indice
            must_continue = False
            #print("index_median_left {}".format(index_median_left))
        if index_median_ok <=0 :
            index_median_ok = indice
            break
    
    if odd:
        #print("median result odd {} ...".format(index_median_ok))
        return index_median_ok
    else:
        #print("median result even: ({} + {}) / 2".format(index_median_left, index_median_ok))
        return (index_median_ok + index_median_left)/2

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):

    notifications = 0
    list_frequencies = [0] * 201 # we have 200 posible elements

    index_median = (d // 2) + 1
    if d % 2 == 0: # even, average from middles
        odd = False    
    else: # odd
        # midle element
        odd = True

    #print("expenditure {} d {} index_median {} odd {}".format(expenditure, d, index_median, odd))

    # first count frequencies, in fir
    for x in range(0,d):
        indice = expenditure[x]
        list_frequencies[indice] += 1


    start_index = 0
    next_index = d
    len_expenditure = len(expenditure)

    while next_index < len_expenditure:
        #print("list_frequencies {}".format(list_frequencies[:10]))
        # calculate median
        median = return_median(list_frequencies, index_median, odd)
        #print("Median: ({} x 2) [{}] <= next value {}".format(median, median*2, expenditure[next_index]))
        if (median * 2) <= expenditure[next_index]:
            notifications += 1
            #print("notification ....................................+=1")
        #else:
            #print("No notification ........................")
        #print("start {} next_index {}".format(expenditure[start_index], expenditure[next_index]))

        # modiffy list_frequencies, without past number and add next number
        list_frequencies[expenditure[start_index]] -= 1
        list_frequencies[expenditure[next_index]] += 1

        start_index += 1
        next_index += 1 

    #print("RESPUESTA {}".format(notifications))

    return notifications


if __name__ == '__main__':

    answer = activityNotifications([2, 3, 4, 2, 3, 6, 8, 4, 5],5)
    assert answer == 2, "check your code"

    answer = activityNotifications([1, 2, 3, 4, 4],4)
    assert answer == 0, "check your code"