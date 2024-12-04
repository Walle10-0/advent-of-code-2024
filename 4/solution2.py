input_file = "input.txt"

# xmas

with open(input_file, "r") as file:
    allLines = file.readlines()
    count = 0
    # print(allLines)

    for i in range(len(allLines)):
        start = 0
        index = allLines[i].find("A", start)
        # print(allLines[i])
        while(index != -1):
            start = index + 1
            got_mass = [False, False]
            # print(allLines[i][index])
            if index <= len(allLines[i]) - 2 and index >= 1 and i <= len(allLines) - 2 and i >= 1:
                if allLines[i+1][index-1] == "M" and allLines[i-1][index+1] == "S":
                    got_mass[0] = True
                if allLines[i+1][index-1] == "S" and allLines[i-1][index+1] == "M":
                    got_mass[0] = True
                if allLines[i+1][index+1] == "M" and allLines[i-1][index-1] == "S":
                    got_mass[1] = True
                if allLines[i+1][index+1] == "S" and allLines[i-1][index-1] == "M":
                    got_mass[1] = True
            if got_mass[0] and got_mass[1]:
                count += 1
            index = allLines[i].find("A", start)
            
    
    file.close()

print(count)
