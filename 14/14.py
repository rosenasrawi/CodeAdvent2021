# Function to open datafile (input or example)
def preprocessData(datafile):
    with open("/Users/rosenasrawi/Documents/VU PhD/Side projects/CodeAdvent2021/14" + datafile, "r") as polyFile:
        poly = polyFile.readlines()

    polymer = poly.pop(0).rstrip("\n"); poly.pop(0)
    poly = [i.rstrip("\n").split(' -> ') for i in poly]

    connections = []; counts = []; insertions = {}
    for i in poly:
        connections.append(i[0])                                                # All types of connections
        counts.append(0)                                                        # count of connections
        insertions[i[0]] = [''.join(i[0][0] + i[1]), ''.join(i[1] + i[0][1])]   # What connection becomes after insertion

    for i in range(len(polymer)-1):
        counts[connections.index(polymer[i:i+2])] += 1                          # Change polymer to count of connections

    return counts, connections, insertions

# Function to keep track of the count of each connection type in polymer 
def insertPolymer(counts, connections, insertions):
    num2add = []; index2rem = []; index2add = []

    for i in range(len(counts)):
        if counts[i] > 0:
            num2add.append(counts[i])
            index2rem.append(i)

            con = connections[i]; ins = insertions[con]
            index2add.append([connections.index(ins[0]), connections.index(ins[1])])

    for i in range(len(num2add)):
        counts[index2rem[i]] -= num2add[i]

    for i in range(len(num2add)):
        j = index2add[i]
        counts[j[0]] += num2add[i]
        counts[j[1]] += num2add[i]

    return counts

# Function to count the occurence of each letter in polymer, based on connections
def letterCount(steps, counts, connections, insertions):

    for i in range(steps):
        counts = insertPolymer(counts, connections, insertions)

    letters = list(set(''.join(connections)))
    letterPosCount = [[0,0] for i in letters]

    for i in range(len(connections)):
        if counts[i] > 0:
            con = connections[i]
            letterPosCount[letters.index(con[0])][0] += counts[i]
            letterPosCount[letters.index(con[1])][1] += counts[i]

    for i in range(len(letterPosCount)):
        letterPosCount[i] = max(letterPosCount[i])

    print(max(letterPosCount)-min(letterPosCount))

# Preprocess data
counts, connections, insertions = preprocessData(datafile = "/input14.txt")

# Part 1 - count letters after 10 iterations, most - least occuring
letterCount(10, counts, connections, insertions)

# Part 2 - count letters after 40 iterations, most - least occuring
letterCount(40, counts, connections, insertions)
