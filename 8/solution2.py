input_file = "input.txt"

with open(input_file, "r") as file:
    count = 0
    everything = file.read()
    allLines = everything.split("\n")
    bounds = [len(allLines), len(allLines[0])]
    frequencies = [x for x in list(set(everything)) if x.isalpha() or x.isdigit()]
    effectMap = []
    
    #print(bounds)
    
    for freq in frequencies:
        locations = []
        for i in range(bounds[0]):
            index = allLines[i].find(freq)
            while index != -1:
                locations.append([i, index])
                index = allLines[i][index+1:].find(freq)
        for target in locations:
            for location in locations:
                if target != location:
                    effectMap.append(location)
                    targetcopy = target.copy()
                    inRange = True
                    while inRange:
                        possibleLocation = [targetcopy[0] + (targetcopy[0] - location[0]), targetcopy[1] + (targetcopy[1] - location[1])]
                        if possibleLocation[0] >= 0 and possibleLocation[0] < bounds[0] and possibleLocation[1] >= 0 and possibleLocation[1] < bounds[1]:
                            #print(possibleLocation)
                            effectMap.append(possibleLocation)
                            location = targetcopy
                            targetcopy = possibleLocation
                        else:
                            inRange = False
                        #print(possibleLocation)
    print(frequencies)
    
    unique = []
    
    for location in effectMap:
        if location not in unique:
            unique.append(location)

    count = len(unique)
    
    visual = list(map(list, everything.split("\n")))
    
    for hit in unique:
        #print(hit)
        #print(len(visual))
        visual[hit[0]][hit[1]] = "#"
    
    visual = list(map(''.join, visual))
    visual = '\n'.join(visual)
    print(visual)
    
    file.close()

print(len(effectMap))
print(count)
