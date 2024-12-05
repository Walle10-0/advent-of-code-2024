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
            for index in range(len(numbers)):
                for ruleI in range(len(beforeRules)):
                    if numbers[index] == beforeRules[ruleI]:
                        try:
                            if numbers.index(afterRules[ruleI]) < index:
                                valid = False
                        except:
                            pass
            if valid:
                # print(numbers[(len(numbers)) // 2])
                count += numbers[(len(numbers)) // 2]
    
    file.close()

print(count)
