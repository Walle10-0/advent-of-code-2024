input_file = "input.txt"

with open(input_file, "r") as file:
    allLinesMaster = file.readlines()
    allLinesMaster = list(map(list, allLinesMaster))
    
    possibleLoops = []
    
    
    for i in range(len(allLinesMaster)):
        for j in range(len(allLinesMaster[i])):
            if allLinesMaster[i][j] == '^':
                gaurdPos = [i, j]
                starting = [i, j]
            if allLinesMaster[i][j] == '\n':
                allLinesMaster[i].pop(j)
    
    gaurd = True
    direction = 0 # ^ v < >

    steps = 0
    while gaurd:
        steps += 1
        allLinesMaster[gaurdPos[0]][gaurdPos[1]] = 'X'
        if direction == 0:
            if gaurdPos[0] == 0:
                gaurd = False
            elif allLinesMaster[gaurdPos[0]-1][gaurdPos[1]] == '#':
                direction = 3
            else:
                gaurdPos[0] -= 1
        if direction == 1:
            if gaurdPos[0] == len(allLinesMaster) - 1:
                gaurd = False
            elif allLinesMaster[gaurdPos[0]+1][gaurdPos[1]] == '#':
                direction = 2
            else:
                gaurdPos[0] += 1
        if direction == 3:
            if gaurdPos[1] == len(allLinesMaster[gaurdPos[0]]) - 1:
                gaurd = False
            elif allLinesMaster[gaurdPos[0]][gaurdPos[1]+1] == '#':
                direction = 1
            else:
                gaurdPos[1] += 1
        if direction == 2:
            if gaurdPos[1] == 0:
                gaurd = False
            elif allLinesMaster[gaurdPos[0]][gaurdPos[1]-1] == '#':
                direction = 0
            else:
                gaurdPos[1] -= 1
    
    print(steps)
    
    for ii in range(len(allLinesMaster)):
        for jj in range(len(allLinesMaster[ii])):
            gaurd = True
            allLines = [x.copy() for x in allLinesMaster]
            if allLines[ii][jj] != 'X':
                gaurd = False
            else:
                allLines[ii][jj] = '#'
            gaurdPos = starting.copy()
            direction = 0 # ^ v < >
            failSafe = steps*100 #10000000000000000
            lastChristmas = []
            lastChristmas2 = []
            lastChristmas.append(gaurdPos.copy)
            lastChristmas.append(gaurdPos.copy)
            lastChristmas2.append(0)
            lastChristmas2.append(0)
    
            while gaurd:
                if failSafe < 0:
                    print("taking too long")
                    gaurd = False
                    possibleLoops.append([ii, jj])
                
                if direction == 0:
                    if gaurdPos[0] == 0:
                        gaurd = False
                    elif allLines[gaurdPos[0]-1][gaurdPos[1]] == '#':
                        direction = 3
                    else:
                        gaurdPos[0] -= 1
                if direction == 1:
                    if gaurdPos[0] == len(allLines) - 1:
                        gaurd = False
                    elif allLines[gaurdPos[0]+1][gaurdPos[1]] == '#':
                        direction = 2
                    else:
                        gaurdPos[0] += 1
                if direction == 3:
                    if gaurdPos[1] == len(allLines[gaurdPos[0]]) - 1:
                        gaurd = False
                    elif allLines[gaurdPos[0]][gaurdPos[1]+1] == '#':
                        direction = 1
                    else:
                        gaurdPos[1] += 1
                if direction == 2:
                    if gaurdPos[1] == 0:
                        gaurd = False
                    elif allLines[gaurdPos[0]][gaurdPos[1]-1] == '#':
                        direction = 0
                    else:
                        gaurdPos[1] -= 1
                
                if gaurd and allLines[gaurdPos[0]][gaurdPos[1]] == ['^', 'v', '<', '>'][direction]:
                    print("been here before")
                    gaurd = False
                    possibleLoops.append([ii, jj])
                allLines[gaurdPos[0]][gaurdPos[1]] = ['^', 'v', '<', '>'][direction]
        
    print(possibleLoops)
    
    # just in case
    if starting in possibleLoops:
        possibleLoops.remove(starting)
    
    count = len(possibleLoops)
    
    file.close()

print(count)
