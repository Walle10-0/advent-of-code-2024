input_file = "input.txt"

# Don't worry, we have technology (the internet)
# https://www.geeksforgeeks.org/find-the-nth-digit-from-right-in-base-b-of-the-given-number-in-decimal-base/
# Function to compute Nth digit
# from right in base B
def nthDigit(a, n, b):
 
    # Skip N-1 Digits in Base B
    for i in range(1, n):
        a = a // b
 
    # Nth Digit from right in Base B
    return a % b

with open(input_file, "r") as file:
    count = 0
    for line in file:
        # extract info
        calibration, numbers = line.split(": ")
        calibration = int(calibration)
        numbers = list(map(int, numbers.split()))
        valid = False
        
        #print(calibration)
        #print(numbers)
        
        for i in range(pow(3, len(numbers)-1)):
            result = numbers[0]
            for j in range(1, len(numbers)): 
                #print(f"i = {i}, j = {j}")
                digit = nthDigit(i, j, 3)
                if digit == 0:
                    result += numbers[j]
                    #print("0 add")
                elif digit == 1:
                    result *= numbers[j]
                    #print("1 multiply")
                else:
                    result = int(str(result) + str(numbers[j]))
                    #print("2 concat")
            #print(result)
            if result == calibration:
                #print(calibration)
                #print(numbers)
                valid = True
        
        if valid:
            count += calibration
        
    file.close()

print(f"count {count}")