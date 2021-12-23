from queue import PriorityQueue
from math import isinf

def preprocessData(datafile, bigdata):
    with open("/Users/rosenasrawi/Documents/VU PhD/Side projects/CodeAdvent2021/15" + datafile, "r") as inputfile:
            input = inputfile.readlines()
            input = [list(i.rstrip('\n')) for i in input]
            input = [list(map(int, i)) for i in input]

    if bigdata:
        tiles = []
        for ty in range(5):
            for y in range(len(input)):
                row = []
                for tx in range(5):
                    for x in range(len(input[0])):
                        r = input[y][x] + tx + ty
                        if r > 9: r -= 9
                        row.append(r)
                tiles.append(row)
        return tiles      

    else: return input

def neighbours(size, idx):
    x = idx[0]; y = idx[1]; neighbours = []
    candidates = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    for candidate in candidates:
        if 0 <= candidate[0] < size and 0 <= candidate[1] < size:
            neighbours.append(candidate)
    return neighbours

def dijkstra(input):

    visited = {(0, 0)}
    distances = [[float('inf') for j in range(len(input[0]))]
                 for i in range(len(input))]
    distances[0][0] = 0
    pq = PriorityQueue()
    pq.put((0, (0, 0)))

    while not pq.empty():
        node = pq.get()
        node = node[1]
        neighbourlist = neighbours(len(input),node)
        for neighbour in neighbourlist:
            if not (neighbour in visited):
                visited.add(neighbour)
                newdist = distances[node[0]][node[1]] + \
                    input[neighbour[0]][neighbour[1]]
                if newdist < distances[neighbour[0]][neighbour[1]]:
                    distances[neighbour[0]][neighbour[1]] = newdist
                    pq.put((newdist, neighbour))

    return distances[-1][-1]

# Part 1 - shortest path from top left to bottom right, original input
input = preprocessData(datafile = "/input15.txt", bigdata = False)
print(dijkstra(input))

# Part 2 - shortest path from top left to bottom right, big data
input = preprocessData(datafile = "/input15.txt", bigdata = True)
print(dijkstra(input))
