input_file = "input.txt"

with open(input_file, "r") as file:
    count = 0
    for line in file:
        # extract info
        calibration, numbers = line.split(": ")
        calibration = int(calibration)
        numbers = list(map(int, numbers.split()))
        valid = False
        
        print(calibration)
        print(numbers)
        
        for i in range(pow(2, len(numbers)-1)):
            result = numbers[0]
            for j in range(1, len(numbers)): 
                if i & (1 << (j-1)) == 0:
                    result += numbers[j]
                else:
                    result *= numbers[j]
            print(result)
            if result == calibration:
                valid = True
        
        if valid:
            count += calibration
        
    file.close()

print(f"count {count}")
