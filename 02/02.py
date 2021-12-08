#### Submarine and its planned course ####

# Open & read data
with open("/Users/rosenasrawi/Documents/VU PhD/Side projects/CodeAdvent2021/02/input02.txt", "r") as plannedCourse:
    directions = plannedCourse.readlines()

# Part 1 - horizontal direction * depth
horizontal = 0
depth = 0

for dir in range(len(directions)):
    thisDirection = directions[dir].split()
    if thisDirection[0] == "forward":
        horizontal += int(thisDirection[1])
    elif thisDirection[0] == "up":
        depth -= int(thisDirection[1])
    elif thisDirection[0] == "down":
        depth += int(thisDirection[1])

print(depth*horizontal)

# Part 2 - not quite what we thought
horizontal = 0
depth = 0
aim = 0

for dir in range(len(directions)):
    thisDirection = directions[dir].split()
    if thisDirection[0] == "forward":
        horizontal += int(thisDirection[1])
        depth += aim*int(thisDirection[1])
    elif thisDirection[0] == "up":
        aim -= int(thisDirection[1])
    elif thisDirection[0] == "down":
        aim += int(thisDirection[1])

print(depth*horizontal)
