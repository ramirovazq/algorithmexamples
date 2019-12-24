def intcode_programm(original_list):
    original_list_ = original_list.copy() # copy from original_list
    len_original = len(original_list_)

    dicc_options = {
        1: "add", # adds together numbers from 2 positions and stores in a third
        2: "multiplies",
        99: "program_finished", # and should inmediatly halt
        ## unknown opcode, means sth wrong
    }
    answer = []

    i = 0
    while i < len_original:
        # first_element
        first_element = original_list[i]
        #print(first_element)
        if first_element in dicc_options.keys(): # the first element 
            if dicc_options[first_element] == "add": # 1

                i += 1
                second = original_list[i]
                i += 1
                third  = original_list[i]
                i += 1
                fourth = original_list[i]

                sum_both = original_list[second] + original_list[third]
                original_list[fourth] = sum_both

                i += 1 # goes for net_one

            elif dicc_options[first_element] == "multiplies": # 2
                i += 1
                second = original_list[i]
                i += 1
                third  = original_list[i]
                i += 1
                fourth = original_list[i]

                mult_both = original_list[second] * original_list[third]
                original_list[fourth] = mult_both

                i += 1 # goes for net_one

            else: # 99
                #print("program finished, 99")
                break
        else:
            print("sth wrong")
            break
        #print(original_list)

    return original_list

if __name__ == "__main__":
    
    '''
    # those are tests
    a = intcode_programm([1,0,0,0,99])
    assert a == [2,0,0,0,99], "check the code, man"

    a = intcode_programm([2,3,0,3,99])
    assert a == [2,3,0,6,99], "check the code, man"

    a = intcode_programm([2,4,4,5,99,0])
    assert a == [2,4,4,5,99,9801], "check the code, man"
    
    #                     1,1,1,4, 2,5,6,0,99
    a = intcode_programm([1,1,1,4,99,5,6,0,99])
    assert a == [30,1,1,4,2,5,6,0,99], "check the code, man"
    
    a = intcode_programm([1,9,10,3,2,3,11,0,99,30,40,50])
    assert a == [3500,9,10,70,2,3,11,0,99,30,40,50], "check the code, man"

    '''
    base_original = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,6,19,23,2,23,6,27,2,6,27,31,2,13,31,35,1,10,35,39,2,39,13,43,1,43,13,47,1,6,47,51,1,10,51,55,2,55,6,59,1,5,59,63,2,9,63,67,1,6,67,71,2,9,71,75,1,6,75,79,2,79,13,83,1,83,10,87,1,13,87,91,1,91,10,95,2,9,95,99,1,5,99,103,2,10,103,107,1,107,2,111,1,111,5,0,99,2,14,0,0]
    output = 19690720
    a = None

        
        
    #a = intcode_programm(base_list)
    #print(a)
    break_first = False
    for x in range(0,100):
        for y in range(0,100):
            base_list = base_original.copy()
            #a = intcode_programm(base_list)
            base_list[1] = x
            base_list[2] = y
            a = intcode_programm(base_list)
            print("x {} y {} --> resultado {}".format(x,y,a[0]))
            if a[0] == output:
                print("exito ......................................")
                break_first = True
                break
        if break_first:
            break

    print("")
    print("")
    print("x {} y {} --> resultado {}, 100*noun + verb = {}".format(x,y,a[0], (100*x+y)))


    '''
    print("-------------")
    a = intcode_programm([1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,6,19,23,2,23,6,27,2,6,27,31,2,13,31,35,1,10,35,39,2,39,13,43,1,43,13,47,1,6,47,51,1,10,51,55,2,55,6,59,1,5,59,63,2,9,63,67,1,6,67,71,2,9,71,75,1,6,75,79,2,79,13,83,1,83,10,87,1,13,87,91,1,91,10,95,2,9,95,99,1,5,99,103,2,10,103,107,1,107,2,111,1,111,5,0,99,2,14,0,0])
    print(a)
    '''