def add2dict(llave, dict_):
    if llave in dict_.keys():
        dict_[llave] = dict_[llave] + 1
    else:
        dict_[llave] = 1
    return dict_

def point_plus(movement, original_point=(0,0), points={}):
    '''
    movement R5, L5, U5, D5 
    points, a dict with points from path
    original point, is the beginning point
    '''

    # if original point appears already in points, then it does not count double
    if original_point in points.keys():
        points[original_point] = points[original_point] - 1

    advance = 0
    if ("R" in movement):
        advance = int(movement.split("R")[1]) + 1
    if ("L" in movement):
        advance = int(movement.split("L")[1]) + 1
    if ("U" in movement):
        advance = int(movement.split("U")[1]) + 1
    if ("D" in movement):
        advance = int(movement.split("D")[1]) + 1


    final_point = None
    #print("original point {} ..... movement {} ... advance {}".format(original_point, movement, advance))

    x = original_point[0]
    y = original_point[1] # static

    if ("R" in movement) or ("L" in movement): # goes right, moves over X

        if ("R" in movement):
            #print(list(range(x, x+advance)))
            for x_coordenada in range(x, x+advance):
                point = (x_coordenada,y)
                # POINT
                points = add2dict(point, points)
                final_point = point 

        elif ("L" in movement):
            #print(list(reversed(range(x-advance+1, x+1))))
            for x_coordenada in reversed(range(x-advance+1, x+1)):
                point = (x_coordenada,y)
                # POINT     
                points = add2dict(point, points)
                final_point = point 


    if ("D" in movement) or ("U" in movement): # goes right, moves over X

        if ("U" in movement):
            #print(list(range(y, y+advance)))
            for y_coordenada in range(y, y+advance):
                point = (x,y_coordenada)
                # POINT 
                points = add2dict(point, points)
                final_point = point 

        elif ("D" in movement):
            #print(list(reversed(range(y-advance+1, y+1))))
            for y_coordenada in reversed(range(y-advance+1, y+1)):
                point = (x,y_coordenada)
                #print("")
                #print(point)
                # POINT 
                points = add2dict(point, points)
                final_point = point 

    #print(points)
    return points, final_point

def wire(dicc_puntos, list_instrucctions=[]):

    first_ = list_instrucctions.pop(0)
    dicc_puntos, punto_final = point_plus(first_, (0,0), dicc_puntos)

    for instrucction in list_instrucctions:
        dicc_puntos, punto_final = point_plus(instrucction, punto_final, dicc_puntos)

    #print("dicc_puntos {}".format(dicc_puntos))
    return dicc_puntos

def normaliza(diccionario):
    for x in diccionario:
        diccionario[x] = 1
    return diccionario

if __name__ == "__main__":
    '''
    point_plus("R8",(0,0), {})
    print("==========")
    point_plus("U5",(0,0), {})
    print("==========")
    point_plus("L5",(0,0), {})
    print("==========")
    point_plus("D3",(0,0), {})
    print("=================================")
    point_plus("R8",(2,2), {})
    print("==========")
    point_plus("U5",(2,2), {})
    print("==========")
    point_plus("L5",(2,2), {})
    print("==========")
    point_plus("D3",(2,2), {})
    print("==========")
    
    '''
    import csv
    
    diccionario_puntos = {}
    with open('cables_0.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for indice, row in enumerate(csv_reader):
            #print("row.....")
            #print(row)
            if indice == 0:
                cable1 = row
            else:
                cable2 = row
    diccionario_puntos = wire(diccionario_puntos, cable1) #R8,U5,L5,D3  cable1
    diccionario_puntos = normaliza(diccionario_puntos)
    diccionario_puntos = wire(diccionario_puntos, cable2) #U7,R6,D4,L4  cable2
    result = filter(lambda x: diccionario_puntos[x]>1, diccionario_puntos)
    print("....................... concurrent points .......................")
    distance = []
    for y in result:
        print("punto {}".format(y))
        distance.append(y[0] + y[1])
    print("....................... sum .......................")
    distance.sort()
    print(distance[0])

    

    diccionario_puntos = {}
    with open('cables_1.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for indice, row in enumerate(csv_reader):
            #print("row.....")
            #print(row)
            if indice == 0:
                cable1 = row
            else:
                cable2 = row
    diccionario_puntos = wire(diccionario_puntos,cable1)
    diccionario_puntos = normaliza(diccionario_puntos)
    diccionario_puntos = wire(diccionario_puntos,cable2)
    
    result = filter(lambda x: diccionario_puntos[x]>1, diccionario_puntos)
    print("....................... concurrent points .......................")
    distance = []
    for y in result:
        print("punto {}".format(y))
        distance.append(abs(y[0]) + abs(y[1]))
    print("....................... sum .......................")
    distance.sort()
    #print(distance)
    print(distance[0])


    
    diccionario_puntos = {}
    with open('cables_2.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for indice, row in enumerate(csv_reader):
            #print("row.....")
            #print(row)
            if indice == 0:
                cable1 = row
            else:
                cable2 = row
    diccionario_puntos = wire(diccionario_puntos,cable1)
    diccionario_puntos = normaliza(diccionario_puntos)
    diccionario_puntos = wire(diccionario_puntos,cable2)

    result = filter(lambda x: diccionario_puntos[x]>1, diccionario_puntos)
    print("....................... concurrent points .......................")
    distance = []
    for y in result:
        print("punto {}".format(y))
        distance.append(abs(y[0]) + abs(y[1]))
    print("....................... sum .......................")
    distance.sort()
    #print(distance)
    print(distance[0])



    # correct steps for cable_3.csv
    with open('cables_3.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for indice, row in enumerate(csv_reader):
            if indice == 0:
                cable1 = row
            else:
                cable2 = row

    diccionario_puntos = {}
    diccionario_puntos = wire(diccionario_puntos,cable1)
    diccionario_puntos = normaliza(diccionario_puntos)
    del diccionario_puntos[(0,0)]
    dicc_a = diccionario_puntos.copy()

    diccionario_puntos = {}
    diccionario_puntos = wire(diccionario_puntos,cable2)
    diccionario_puntos = normaliza(diccionario_puntos)
    del diccionario_puntos[(0,0)]
    dicc_b = diccionario_puntos.copy()

    diccionario_puntos = {}
    for a in dicc_a:
        if a in dicc_b.keys():
            diccionario_puntos[a] = 2

    result = filter(lambda x: diccionario_puntos[x]>1, diccionario_puntos)
    print("....................... concurrent points .......................")
    distance = []
    for y in result:
        print("punto {}".format(y))
        distance.append(abs(y[0]) + abs(y[1]))
    print("....................... sum .......................")
    distance.sort()
    #print(distance)
    print(distance[0])
