# Open data file
with open("/Users/rosenasrawi/Documents/VU PhD/Side projects/CodeAdvent2021/14/input14.txt", "r") as polyFile:
    poly = polyFile.readlines()

    polymer = list(poly.pop(0).rstrip("\n")); poly.pop(0)

    poly = [i.rstrip("\n").split(' -> ') for i in poly]

    connections = []; insertions = []
    for i in poly:
        connections.append(list(i[0]))
        insertions.append(i[1])


# Example data
# polymer = ['N', 'N', 'C', 'B']
# connections = [['C','H'],['H','H'],['C','B'],['N','H'],['H','B'],['H','C'],['H','N'],['N','N'],['B','H'],['N','C'],['N','B'],['B','N'],['B','B'],['B','C'],['C','C'],['C','N']]
# insertions = ['B','N','H','C','C','B','C','C','H','B','B','B','N','B','N','C']


# Function to insert to polymer
def insertPolymer(polymer, connections, insertions):
    insIndex = []; polyIndex = []

    for i in range(len(polymer)-1):
        insIndex.append(connections.index(polymer[i:i+2]))
        polyIndex.append(i*2+1)

    for i in range(len(polyIndex)):
        ins = insertions[insIndex[i]]
        polymer.insert(polyIndex[i],ins)

    return polymer

# Part 1 - count least and most occuring in polymer after 10 steps of insertion
for i in range(10):
    polymer = insertPolymer(polymer, connections, insertions)

mostComm = polymer.count(max(set(polymer), key = polymer.count))
leastComm = polymer.count(min(set(polymer), key = polymer.count))

print(mostComm-leastComm)
