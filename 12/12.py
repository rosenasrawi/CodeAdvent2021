
with open("/Users/rosenasrawi/Documents/VU PhD/Side projects/CodeAdvent2021/12/input12.txt", "r") as caveFile:
    cave = caveFile.readlines()
    cave = [i.rstrip("\n") for i in cave]
    cave = [cave[i].split('-') for i in range(len(cave))]
print(cave)

# cave = ['start-A','start-b','A-c','A-b','b-d','A-end','b-end']
# cave = [cave[i].split('-') for i in range(len(cave))]


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

graph = createGraph(connections = cave)


def find_all_paths(graph, start, end, path=[]):

    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []

    paths = []
    for node in graph[start]:
        if node not in path or node.isupper():
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

paths = find_all_paths(graph, 'start', 'end', path = [])
print(len(paths))

