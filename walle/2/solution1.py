input_file = "input.txt"

with open(input_file, "r") as file:
    count = 0
    for line in file:
        numbers = line.split()
        prev = int(numbers.pop(0))
        increase = int(numbers[0]) - prev
        increase = increase > 0
        safe = True
        for value in numbers:
            value = int(value)
            if (value - prev) > 0 and not increase:
                safe = False
            if (value - prev) < 0 and increase:
                safe = False
            if abs(value - prev) < 1 or abs(value - prev) > 3:
                safe = False
            prev = value
        if safe:
            count += 1
            print(line + " is safe")
        
    file.close()

print(count)
