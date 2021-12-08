# Binary numbers to decimals

# Open & read data
with open("/Users/rosenasrawi/Documents/VU PhD/Side projects/CodeAdvent2021/03/input03.txt", "r") as binaryCodes:
    binary = binaryCodes.readlines()

# binary = ['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010']

# Create a matrix of numbers
numBins = len(binary)

for bin in range(numBins):
    binary[bin] = list(binary[bin])
    binary[bin].pop()
    binary[bin] = list(map(int, binary[bin]))

# Part 1 - most & least occuring in every column

numCols = len(binary[0])

for num in range(numCols):
    x = [item[num] for item in binary]
    y = int(max(x, key = x.count))

    if num == 0:
        gamma = str(y); epsilon = str(1-y)
    else:
        gamma += str(y); epsilon += str(1-y)

# Change binary to decimal
gamma = int(gamma,2)
epsilon = int(epsilon,2)

print(gamma*epsilon)

# Part 2 - most & lease occuring in each position 

numbersOxygen = binary.copy()
numbersCO2 = binary.copy()

for num in range(numCols):
    ox = [item[num] for item in numbersOxygen]; co2 = [item[num] for item in numbersCO2]
    
    maxOx = int(max(x, key = ox.count)); minOx = int(min(x, key = ox.count))
    maxCo2 = int(max(co2, key = co2.count)); minCo2 = int(min(co2, key = co2.count))

    ox = list(map(int,ox)); co2 = list(map(int,co2))

    if maxOx == minOx: maxOx = 1
    if maxCo2 == minCo2: minCo2 = 0

    if len(numbersOxygen) > 1:
        indexOxygen = [i for i, value in enumerate(ox) if value == maxOx]
        numbersOxygen = [numbersOxygen[i] for i in indexOxygen]
    if len(numbersCO2) > 1:
        indexCO2 = [i for i, value in enumerate(co2) if value == minCo2]
        numbersCO2 = [numbersCO2[i] for i in indexCO2]

# Change binary to decimal

numbersCO2 = int(''.join(map(str, numbersCO2[0])),2)
numbersOxygen = int(''.join(map(str, numbersOxygen[0])),2)

print(numbersCO2*numbersOxygen)



