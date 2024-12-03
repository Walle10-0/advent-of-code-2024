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
for i in range(0, len(list1)):
    diff += abs(list1[i] - list2[i])

print(diff)
