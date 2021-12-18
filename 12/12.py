# Open data file
with open("/Users/rosenasrawi/Documents/VU PhD/Side projects/CodeAdvent2021/12/input12.txt", "r") as caveFile:
    cave = caveFile.readlines()
    cave = [i.rstrip("\n") for i in cave]
    cave = [cave[i].split('-') for i in range(len(cave))]

# cave = ['start-A','start-b','A-c','A-b','b-d','A-end','b-end']
# cave = [cave[i].split('-') for i in range(len(cave))]

# Greate graph from connections
def createGraph(connections):

    # Find unique nodes
    graph = {}
    for con in connections:
        for n in con:
            if n not in graph: graph[n] = []

    # Determine their connections
    for n in graph:
        for con in connections:
            if n in con:
                io = [i for i, value in enumerate(con) if value != n]
                o = con[io[0]]
                graph[n].append(o)
    return graph

# General function to find all paths from node to another
def find_all_paths(graph, start, end, smalltwice, path=[]):

    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []

    paths = []
    for node in graph[start]:
        twoLowers = [i for i in path if i.islower() and path.count(i) == 2 and i !='start']
        if node not in path or node.isupper() or smalltwice and node.islower() and path.count(node) == 1 and node != 'start' and len(twoLowers) == 0:
            newpaths = find_all_paths(graph, node, end, smalltwice, path)
            for newpath in newpaths:
                paths.append(newpath)

    return paths

# Create graph
graph = createGraph(connections = cave)

# Part 1 - find all paths from start to end, big caves unlimited visits
paths = find_all_paths(graph, 'start', 'end', smalltwice=False)
print(len(paths))

# Part 2 - find all paths from start to end, big caves unlimited visits, first small cave two visits
paths = find_all_paths(graph, 'start', 'end', smalltwice=True)
print(len(paths))
