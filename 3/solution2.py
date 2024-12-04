import re # looks like a job for regular expressions!

input_file = "input.txt"

with open(input_file, "r") as file:
    text = file.read()

    expression = "(mul\([0-9]+,[0-9]+\))|(do\(\))|(don't\(\))"

    result = re.findall(expression, text)
    print(result)

    mul_sum = 0
    enabled = True
    
    for command in result:
        if command[0] != '' and enabled:
            x, y = re.findall("[0-9]+", command[0])
            x = int(x)
            y = int(y)
            mul = x * y

            mul_sum += mul
        if command[1]:
            enabled = True
        if command[2]:
            enabled = False
    
    file.close()

print(mul_sum)
