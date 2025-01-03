import functools

input_file = "test.txt"

@functools.cache
def calcSingle(stone):
    if isinstance(stone, list):
        newS = []
        while len(stones) > 0:
            newS.extend(calcSingle(stones.pop(0)))
        return newS
    elif stone == 0:
        stone = [1]
    elif len(str(stone)) % 2 == 0:
        splitStone = list(str(stone))
        diglen = len(splitStone) // 2
        stone = [int(''.join(splitStone[:diglen])), int(''.join(splitStone[diglen:]))]
    else:
        stone *= 2024
        stone = [stone]
    return stone


with open(input_file, "r") as file:
    iterations = 75
    stones = file.readline()
    stones = stones.split()
    stones = list(map(int, stones))
    count = 0
    
    print(stones)
   
    
    for i in range(iterations):
        newS = []
        while len(stones) > 0:
            newS.extend(calcSingle(stones.pop(0)))
        stones = newS
    
    print(stones)
    count = len(stones)
    
    file.close()

print(f"count {count}")
