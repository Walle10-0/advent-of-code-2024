input_file = "input.txt"

import time

# up down right left

def mapPotentialLoop(allLines, i, j, b):
    while isinstance(allLines[i][j], int):
        allLines[i][j] = allLines[i][j] | b
        if b == 0b0100:
            if j != len(allLines[i]) - 1 and allLines[i][j+1] == '#':
                mapPotentialLoop(allLines, i, j, 0b0001)
            if i == 0:
                return
            else:
                i -= 1
        elif b == 0b1000:
            if j != 0 and allLines[i][j-1] == '#':
                mapPotentialLoop(allLines, i, j, 0b0010)
            if i != len(allLines)-1:
                i += 1
            else:
                return
        elif b == 0b0010:
            if i != len(allLines) - 1 and allLines[i+1][j] == '#':
                mapPotentialLoop(allLines, i, j, 0b0100)
            if j != len(allLines[i]) - 1:
                j += 1
            else:
                return
        elif b == 0b0001:
            if i != 0 and allLines[i-1][j] == '#':
                mapPotentialLoop(allLines, i, j, 0b1000)
            if j != 0:
                j -= 1
            else:
                return

with open(input_file, "r") as file:
    allLines = file.readlines()
    allLines = list(map(list, allLines))
    gaurd = True
    gaurdPos = []
    starting = []
    direction = 0b0000
    possibleLoops = []
    
    # find gaurd
    for i in range(len(allLines)):
        for j in range(len(allLines[i])):
            if allLines[i][j] == '.':
                allLines[i][j] = 0
            if allLines[i][j] == '^':
                gaurdPos = [i, j]
                starting = [i, j]
                allLines[i][j] = 0
            if allLines[i][j] == '\n':
                allLines[i].pop(j)

    while gaurd:
        #print(str(direction) + " --> " + str(0b1000 // pow(2,direction)))
        #print(gaurdPos)
        mapPotentialLoop(allLines, gaurdPos[0], gaurdPos[1], (0b1000 >> direction))
        allLines[gaurdPos[0]][gaurdPos[1]] |= 0b10000
        
        if direction == 0:
            if gaurdPos[0] == 0:
                gaurd = False
            elif allLines[gaurdPos[0]-1][gaurdPos[1]] == '#':
                direction = 3
            else:
                if allLines[gaurdPos[0]][gaurdPos[1]] & 0b0001 == 0b0001:
                    if allLines[gaurdPos[0]-1][gaurdPos[1]] & 0b10000 == 0:
                        possibleLoops.append([gaurdPos[0]-1, gaurdPos[1]])
                gaurdPos[0] -= 1
        elif direction == 1:
            if gaurdPos[0] == len(allLines) - 1:
                gaurd = False
            elif allLines[gaurdPos[0]+1][gaurdPos[1]] == '#':
                direction = 2
            else:
                if allLines[gaurdPos[0]][gaurdPos[1]] & 0b0010 == 0b0010:
                    if allLines[gaurdPos[0]+1][gaurdPos[1]] & 0b10000 == 0:
                        possibleLoops.append([gaurdPos[0]+1, gaurdPos[1]])
                gaurdPos[0] += 1
        elif direction == 3:
            if gaurdPos[1] == len(allLines[gaurdPos[0]]) - 1:
                gaurd = False
            elif allLines[gaurdPos[0]][gaurdPos[1]+1] == '#':
                direction = 1
            else:
                if allLines[gaurdPos[0]][gaurdPos[1]] & 0b0100 == 0b0100:
                    if allLines[gaurdPos[0]][gaurdPos[1]+1] & 0b10000 == 0:
                        possibleLoops.append([gaurdPos[0], gaurdPos[1]+1])
                gaurdPos[1]+=1
        elif direction == 2:
            if gaurdPos[1] == 0:
                gaurd = False
            elif allLines[gaurdPos[0]][gaurdPos[1]-1] == '#':
                direction = 0
            else:
                if allLines[gaurdPos[0]][gaurdPos[1]] & 0b1000 == 0b1000:
                    if allLines[gaurdPos[0]][gaurdPos[1]-1] & 0b10000 == 0:
                        possibleLoops.append([gaurdPos[0], gaurdPos[1]-1])
                gaurdPos[1]-=1
                
        # visual
        gaurdIcon = ['^', 'v', '<', '>'][direction]
        viewDistance = [10,10]
        print("----------------------------------")
        print(len(possibleLoops))
        for i in range(-viewDistance[0], viewDistance[0]):
            if i == 0:
                print(''.join([x.ljust(3) for x in map(str, (allLines[gaurdPos[0]][gaurdPos[1] - viewDistance[1]:gaurdPos[1]] + [gaurdIcon] + allLines[gaurdPos[0]][gaurdPos[1] + 1:gaurdPos[1] + viewDistance[1] + 1]))]) )
            else:
                print(''.join([x.ljust(3) for x in map(str, (allLines[gaurdPos[0]+i][gaurdPos[1] - viewDistance[1]:gaurdPos[1] + viewDistance[1] + 1]))]) )
        print("----------------------------------")
        time.sleep(0.1)
    uniqueloops = []
    
    for loop in possibleLoops:
        if loop not in uniqueloops:
            uniqueloops.append(loop)

    if starting in uniqueloops:
        uniqueloops.remove(starting)
        
    uniqueloops.sort()
    print(uniqueloops)
    
    #print(allLines)
    
    count = len(uniqueloops)
    
    file.close()

print(count)
