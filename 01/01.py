#### Measurements of submarine depths ####

# Open & read data
with open("/Users/rosenasrawi/Documents/VU PhD/Side projects/CodeAdvent2021/01/input01.txt", "r") as inputNums:
    depths = inputNums.readlines()
    depths = list(map(int,depths))

# Part 1 - Number of increases num vs previous
increases = 0

for num in range(len(depths)):
    previousDepth = depths[num-1]; depth = depths[num]
    if depth > previousDepth:
        increases += 1

print(increases)

# Part 2 - Number of in creases window vs previous
increases = 0

for num in range(3,len(depths)):
    window = sum(depths[num-2:num+1]); previousWindow = sum(depths[num-3:num])
    if window > previousWindow:
        increases += 1

print(increases)
