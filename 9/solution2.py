input_file = "input.txt"

with open(input_file, "r") as file:
    everything = file.read()
    allLines = list(map(list, everything.split("\n")))
    count = 0
    
    for line in allLines:
        line = list(map(int, line))
        myDrive = []
        myFiles = []
        for i in range(len(line)):
            if i % 2 == 0:
                myFiles.append([len(myDrive), line[i]])
                myDrive.extend([i // 2]*line[i])
            else:
                myDrive.extend(['.']*line[i])
        
        print(myDrive)
        
        myFiles.reverse()
        
        while len(myFiles) > 0:
            e = myFiles.pop(0)
            needed = e[1]
            startf = e[0]
                    
            loop = True
            found = False
            starte = 0
            ende = 0
            while loop:
                if myDrive[starte] != '.':
                    starte += 1
                    ende = starte
                else:
                    if ende - starte >= needed-1:
                        loop = False
                        found = True
                        #print("found!")
                    else:
                        ende += 1
                        if myDrive[ende] != '.':
                            starte = ende
                        
                if ende >= startf:
                    loop = False
                    #print("end of loop")
        
            if found:
                while needed > 0:
                    myDrive[starte] = myDrive[startf]
                    myDrive[startf] = '.'
                    startf += 1
                    starte += 1
                    needed -= 1
        
        
        print(myDrive)
        print("that was myDrive")
        
        count_dooku = 0
        while count_dooku < len(myDrive):
            if myDrive[count_dooku] != '.':
                count += myDrive[count_dooku] * count_dooku
            count_dooku += 1
        
    file.close()

print(count)
