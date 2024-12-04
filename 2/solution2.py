input_file = "input.txt"

def isSafe(numbers):
    numbers = numbers.copy()
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
    return safe

with open(input_file, "r") as file:
    count = 0
    for line in file:
        all_numbers = line.split()

        if isSafe(all_numbers):
            count += 1
        else:
            safe = False
            for i in range(len(all_numbers)):
                safe |= isSafe(all_numbers[:i] + all_numbers[i + 1:])
            if safe:
                count += 1
        
    file.close()

print(count)
