input_file = "input.txt"

with open(input_file, "r") as file:
    iterations = 35
    stones = file.readline()
    stones = stones.split()
    stones = list(map(int, stones))
    count = 0
    
    print(stones)
    
    for i in range(iterations):
        j = 0
        while j < (len(stones)):
            if stones[j] == 0:
                stones[j] = 1
            elif len(str(stones[j])) % 2 == 0:
                splitStone = list(str(stones.pop(j)))
                diglen = len(splitStone) // 2
                stones.insert(j, int(''.join(splitStone[:diglen])))
                j += 1
                stones.insert(j, int(''.join(splitStone[diglen:])))
            else:
                stones[j] *= 2024
            j += 1
    
    print(stones)
    count = len(stones)
    
    file.close()

print(f"count {count}")
