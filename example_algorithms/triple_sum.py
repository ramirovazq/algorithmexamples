def filter_elements(value, lista, menor_o_igual_que=True):
    l = []
    if menor_o_igual_que:
        for x in lista:
            if x <= value:
                l.append(x)
            else:
                break
    else: # mayor o igual que
        for x in lista:
            if x <= value:
                l.append(x)
            else:
                break
    return l

def triplets(a, b, c):
    #   a   b   c
    #   p   q   r
    # p <= q  and q >= r
    a.sort()
    b.sort()
    c.sort()

    print("--------------")
    print(a)
    print(b)
    print(c)

    total = 0 
    d = {}
    for x in b: # traverse q list
        encuentra_a, indice_a = binary_search(a, x) 
        encuentra_c, indice_c = binary_search(c, x)

        print("indice_a {}".format(indice_a))
        print("indice_c {}".format(indice_c))

        if encuentra_a and encuentra_c:
            total = total + ((indice_a+1) * (indice_c+1))
            print("entra ...{}".format(total))
        else:
            print("no entra ...")
    

    return total

def nearest_binary_search(lista, value):
    '''
    lista, must be ordered 
    value, is the number we are searching
    '''

    low = 0 
    high = len(lista) - 1

    while low <= high:
        mid = (low + high) // 2
        if lista[mid] == value:     
            return mid
        elif lista[mid] < value: # en lado derecho
            low = mid + 1
        else:
            high = mid - 1

    return True


if __name__ == '__main__':

    # 15, is a value that exists in a list
    answer = nearest_binary_search([1,3,5,7,8,10,11,12,13,15], 15)
    assert answer == 9, "check code"

    # 7, is a value that does not exists in a list
    answer = nearest_binary_search([1,3,5,7,8,10,11,12,13,15], 7)
    assert answer == 3, "check code"

    # 7, is a value that does not exists in a list
    #answer = nearest_binary_search([1,3,5,7,8,10,11,12,13,15], 9)
    #print(answer)
    #assert answer == 13, "check code"


    '''
    counter = triplets([1,3,5,7],[5,7,9],[7,9,11,13])
    print(counter)
    assert counter == 12, "check code"

    
    counter = triplets([1,4,5],[2,3,3],[1,2,3])
    print(counter)
    assert counter ==5, "check code"
    '''