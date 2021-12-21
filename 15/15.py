from queue import PriorityQueue

# Function to preprocess data
def preprocessData(datafile):

    # Open data
    with open("/Users/rosenasrawi/Documents/VU PhD/Side projects/CodeAdvent2021/15" + datafile, "r") as edgeFile:
        edges = edgeFile.readlines()
        edges = [list(i.rstrip('\n')) for i in edges]
        edges = [list(map(int, i)) for i in edges]

    # Determine names of nodes, and weights between them
    names = []; numNodes = len(edges)*len(edges[0])
    for i in range(numNodes): names.append(i)

    nodes = [[0 for i in edges[0]] for i in edges]
    for i in range(len(edges)):
        for j in range(len(edges[0])):
            nodes[i][j] = names.pop(0)

    return nodes, edges, numNodes

# Class to initialise graph and add edges
class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []
    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight

# Functions to add edges to graph from input file
def addEdgesToGraph(nodes, edges, numNodes):
    
    graph = Graph(numNodes) # initialise a graph

    for row in range(len(nodes)): # horizontal steps
        name = nodes[row]; num = edges[row]
        for i in range(len(name)-1):
            graph.add_edge(name[i], name[i+1], num[i+1])

    for col in range(len(nodes[0])): # vertical steps
        name = [row[col] for row in nodes]
        num = [row[col] for row in edges]
        for i in range(len(name)-1):
            graph.add_edge(name[i], name[i+1], num[i+1])

    return graph

# Function to run Dijkstra algorithm
def dijkstra(graph, start_vertex):
    D = {v:float('inf') for v in range(graph.v)}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)

        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D

datafile = "/input.txt"
nodes, edges, numNodes = preprocessData(datafile)

g = addEdgesToGraph(nodes, edges, numNodes)

D = dijkstra(g, start_vertex = 0)
print(D)