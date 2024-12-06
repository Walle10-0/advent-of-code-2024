input_file = "input.txt"

with open(input_file, "r") as file:
    allLines = file.readlines()
    allLines = list(map(list, allLines))
    gaurd = True
    
    while gaurd:
        gaurd = False

        for i in range(len(allLines)):
            start = 0
            for j in range(len(allLines[i])):
                if allLines[i][j] == '^':
                    gaurd = True
                    if i == 0:
                        allLines[i][j] = 'X'
                    elif allLines[i-1][j] == '#':
                        allLines[i][j] = '>'
                    else:
                        allLines[i-1][j] = '^'
                        allLines[i][j] = 'X'
                if allLines[i][j] == 'v':
                    gaurd = True
                    if i == len(allLines) - 1:
                        allLines[i][j] = 'X'
                    elif allLines[i+1][j] == '#':
                        allLines[i][j] = '<'
                    else:
                        allLines[i+1][j] = 'v'
                        allLines[i][j] = 'X'
                if allLines[i][j] == '>':
                    gaurd = True
                    if j == len(allLines[i]) - 1:
                        allLines[i][j] = 'X'
                    elif allLines[i][j+1] == '#':
                        allLines[i][j] = 'v'
                    else:
                        allLines[i][j+1] = '>'
                        allLines[i][j] = 'X'
                if allLines[i][j] == '<':
                    gaurd = True
                    if j == 0:
                        allLines[i][j] = 'X'
                    elif allLines[i][j-1] == '#':
                        allLines[i][j] = '^'
                    else:
                        allLines[i][j-1] = '<'
                        allLines[i][j] = 'X'
    allLines = list(map(''.join, allLines))
    allLines = ''.join(allLines)
    print(allLines)
    count = allLines.count('X')
    
    file.close()

print(count)
