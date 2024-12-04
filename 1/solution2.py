input_file = "input.txt"

list1 = []
list2 = []

with open(input_file, "r") as file:
    for line in file:
        number1, number2 = line.split()
        list1.append(int(number1))
        list2.append(int(number2))
    file.close()

list1.sort()
list2.sort()

diff = 0
for number in list1:
    occurances = 0
    for instance in list2:
        if number == instance:
            occurances +=1
    diff += number * occurances

print(diff)
