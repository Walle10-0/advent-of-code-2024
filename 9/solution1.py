input_file = "input.txt"

with open(input_file, "r") as file:
    everything = file.read()
    allLines = list(map(list, everything.split("\n")))
    count = 0
    
    for line in allLines:
        line = list(map(int, line))
        myDrive = []
        for i in range(len(line)):
            if i % 2 == 0:
                myDrive.extend([i // 2]*line[i])
            else:
                myDrive.extend(['.']*line[i])
        
        print(myDrive)
        
        empty = 0
        full = len(myDrive) - 1
        while full > empty:
            if myDrive[empty] != '.':
                empty += 1
            if myDrive[full] == '.':
                full -= 1
            if myDrive[empty] == '.' and myDrive[full] != '.':
                myDrive[empty] = myDrive[full]
                myDrive[full] = '.'
        
        print(myDrive)
        print("that was myDrive")
        
        count_dooku = 0
        while myDrive[count_dooku] != '.':
            count += myDrive[count_dooku] * count_dooku
            count_dooku += 1
        
    file.close()

print(count)
