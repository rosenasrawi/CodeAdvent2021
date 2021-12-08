# Open & read data
with open("/Users/rosenasrawi/Documents/VU PhD/Side projects/CodeAdvent2021/07/input07.txt", "r") as crabFile:
    crabs = crabFile.readlines()

crabs = list(map(int, crabs[0].split(',')))
# crabs = [16,1,2,0,4,2,7,1,2,14]

crabPositions = list(range(min(crabs),max(crabs)+1)) # All positions between nearest and farthest crab

def determineLeastFuel(fuelUse):
    fuelPerPos = []

    for pos in crabPositions:
        fuel = [abs(x-pos) for x in crabs] # Check difference between every crab and the position

        if fuelUse == 'increasing':
            fuel = [fuel[i]*(fuel[i]+1)/2 for i in range(len(fuel))]

        fuelPerPos.append(sum(fuel))

    leastFuel = int(min(fuelPerPos))
    bestPos = crabPositions[fuelPerPos.index(leastFuel)]

    return [leastFuel, bestPos]

# Part 1 - Fuel is constant per position change
print(determineLeastFuel(fuelUse = 'constant'))

# Part 2 - Fuel is increasing per position change
print(determineLeastFuel(fuelUse = 'increasing'))


