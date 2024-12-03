import re # looks like a job for regular expressions!

input_file = "input.txt"

with open(input_file, "r") as file:
    text = file.read()

    expression = "mul\([0-9]+,[0-9]+\)"

    result = re.findall(expression, text)
    print(result)

    mul_sum = 0
    
    for command in result:
        x, y = re.findall("[0-9]+", command)
        x = int(x)
        y = int(y)
        mul = x * y

        mul_sum += mul
    
    file.close()

print(mul_sum)
