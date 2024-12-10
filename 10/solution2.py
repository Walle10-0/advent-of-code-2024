input_file = "input.txt"

def getPath(allLines, i, j):
    #print(f"{i}+{j} - {allLines[i][j]} -->")
    if allLines[i][j] == 9:
        return 1
    else:
        result = 0
        if i < len(allLines)-1 and allLines[i+1][j] == allLines[i][j]+1:
            result += (getPath(allLines, i+1, j))
        if i > 0 and allLines[i-1][j] == allLines[i][j]+1:
            result += (getPath(allLines, i-1, j))
        if j < len(allLines[i])-1 and allLines[i][j+1] == allLines[i][j]+1:
            result += (getPath(allLines, i, j+1))
        if j > 0 and allLines[i][j-1] == allLines[i][j]+1:
            result += (getPath(allLines, i, j-1))
        return result

with open(input_file, "r") as file:
    allLines = file.readlines()
    for i in range(len(allLines)):
        allLines[i] = list(allLines[i])
        if '\n' in allLines[i]:
            allLines[i].remove('\n')
        allLines[i] = list(map(int, allLines[i]))
    count = 0
    
    print(allLines)
    
    for i in range(len(allLines)):
        for j in range(len(allLines[i])):
            if allLines[i][j] == 0:
                score = getPath(allLines, i, j)
                print(score)
                count += score
    
    file.close()

print(count)
