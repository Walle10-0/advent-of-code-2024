input_file = "input.txt"

with open(input_file, "r") as file:
    count = 0
    beforeRules = []
    afterRules = []
    
    for line in file:
        if line.find("|") != -1:
            before, after = line.split("|")
            before = int(before)
            after = int(after)
            beforeRules.append(before)
            afterRules.append(after)
        elif line.find(",") != -1:
            numbers = list(map(int, line.split(",")))
            valid = True
            for justRepeatThis in range(len(numbers)):
                for index in range(len(numbers)):
                    for ruleI in range(len(beforeRules)):
                        if numbers[index] == beforeRules[ruleI]:
                            try:
                                found = numbers.index(afterRules[ruleI])
                                if found < index:
                                    #print(line)
                                    valid = False
                                    removed = numbers.pop(found)
                                    numbers.insert(index, removed)
                                    #print(numbers)
                            except:
                                pass
            if not valid:
                # print(numbers[(len(numbers)) // 2])
                count += numbers[(len(numbers)) // 2]
    
    file.close()

print(count)
