input_file = "input.txt"

# xmas

with open(input_file, "r") as file:
    allLines = file.readlines()
    count = 0

    for i in range(len(allLines)):
        start = 0
        index = allLines[i].find("X", start)
        while(allLines[i].find("X", start) != -1):
            start = index + 1
            if index <= len(allLines[i]) - 4:
                if allLines[i][index + 1] == "M" and allLines[i][index + 2] == "A" and allLines[i][index + 3] == "S":
                    count += 1
            if index >= 3:
                if allLines[i][index - 1] == "M" and allLines[i][index - 2] == "A" and allLines[i][index - 3] == "S":
                    count += 1
            if i <= len(allLines) - 4:
                if allLines[i + 1][index] == "M" and allLines[i + 2][index] == "A" and allLines[i + 3][index] == "S":
                    count += 1
            if i >= 3:
                if allLines[i - 1][index] == "M" and allLines[i - 2][index] == "A" and allLines[i - 3][index] == "S":
                    count += 1
            if i >= 3 and index >= 3:
                if allLines[i - 1][index - 1] == "M" and allLines[i - 2][index - 2] == "A" and allLines[i - 3][index - 3] == "S":
                    count += 1
            if i <= len(allLines) - 4 and index >= 3:
                if allLines[i + 1][index - 1] == "M" and allLines[i + 2][index - 2] == "A" and allLines[i + 3][index - 3] == "S":
                    count += 1
            if i <= len(allLines) - 4 and index <= len(allLines[i]) - 4:
                if allLines[i + 1][index + 1] == "M" and allLines[i + 2][index + 2] == "A" and allLines[i + 3][index + 3] == "S":
                    count += 1
            if i >= 3 and index <= len(allLines[i]) - 4:
                if allLines[i - 1][index + 1] == "M" and allLines[i - 2][index + 2] == "A" and allLines[i - 3][index + 3] == "S":
                    count += 1
            index = allLines[i].find("X", start)
            
    
    file.close()

print(count)
