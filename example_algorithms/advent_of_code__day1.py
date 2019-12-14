def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier


def counter_upper(value):
    value_by_three = value / 3
    answer = truncate(value_by_three) 
    return int(answer - 2)

def counter_while(value):
    '''
    takes a number, and return 
    the number of times it executes
    second answer, a list of values to sum
    '''
    list_sum = []
    counter = 0
    while True:
        answer = counter_upper(value)
        #print("answer ....")
        #print(answer)
        if answer <= 0:
            break
        list_sum.append(answer)
        counter += 1
        value = answer
    return counter, list_sum

def counter_upper_data_one(file_name="day1.csv"):
    import csv
    total = 0
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file)
        for index, row in enumerate(csv_reader):
            registro = int(row[0])
            total = total + counter_upper(registro)    
    return total


def counter_upper_data_two(file_name="day1.csv"):
    import csv
    total = 0
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file)
        for index, row in enumerate(csv_reader):
            registro = int(row[0])
            a, b = counter_while(registro)
            total = total + sum(b)
    return total


if __name__ == "__main__":

    a = counter_upper(12)
    assert a == 2, "check code"

    a = counter_upper(14)
    assert a == 2, "check code"

    a = counter_upper(1969)
    assert a == 654, "check code"

    a = counter_upper(100756)
    assert a == 33583, "check code"

    number_times, b = counter_while(14)
    assert sum(b) == 2, "check code"
    #print("number {} ...  number_times {} .... listsum {}".format(14, sum(b), b))

    number_times, b = counter_while(1969)
    assert sum(b) == 966, "check code"
    #print("number {} ...  number_times {} .... listsum {}".format(1969, sum(b), b))

    number_times, b = counter_while(100756)
    assert sum(b) == 50346, "check code"
    #print("number {} ...  number_times {} .... listsum {}".format(100756, sum(b), b))


    
    answer = counter_upper_data_one()
    print(answer) # 3262991
    
    answer = counter_upper_data_two()
    print(answer) # 4891620

