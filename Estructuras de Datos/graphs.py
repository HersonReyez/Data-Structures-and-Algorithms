## Representation ##
# Array of Edges (Directed) [Start, End]
nodes = 8
ArrayEdges = [[0,1],[1,2],[0,3],[3,4],[4,2],[4,5],[5,2],[3,6],[3,7]]

# Convert Array of Edges -> Adjacency Matrix
AdjacencyMatrix = []
for i in range(nodes):
    AdjacencyMatrix.append([0] * nodes)

for u, v in ArrayEdges:
    AdjacencyMatrix[u][v] = 1

    # Uncomment the following line if the graph is undirected
    #AdjacencyMatrix[v][u] = 1

# Convert Array of Egdes -> Adjacency List
from collections import defaultdict

AdjacencyList = defaultdict(list)

for u,v in ArrayEdges:
    AdjacencyList[u].append(v)
    # Uncomment the fllowing line if the graph is undirected
    #AdjacencyList[v].append(u)

print("Graph like Adjacency List")
for i in AdjacencyList:
    print(i, ":", AdjacencyList[i])

## Search ##
# DFS with Recursion - O(V + E)
# Where V is the number of nodes and E is the number of edges
def dfs_recursive(node):
    print(node)
    for i_node in AdjacencyList[node]:
        if i_node not in seen:
            seen.add(i_node)
            dfs_recursive(i_node)

source = 0
seen = set()
seen.add(source)
print("DFS with Recursion")
dfs_recursive(source)

# Iterative DFS with Stack - O(V + E)
seource = 0
seen = set()
seen.add(source)
stack = [source]

print("DFS with Stack")
while stack:
    node = stack.pop()
    print(node)
    for i_node in AdjacencyList[node]:
        if i_node not in seen:
            seen.add(i_node)
            stack.append(i_node)

# BFS with Queue - O(V+E)
from collections import deque

source = 0
seen = set()
seen.add(source)
queue = deque()
queue.append(source)

print("DFS with Queue")
while queue:
    node = queue.popleft()
    print(node)
    for i_node in AdjacencyList[node]:
        if i_node not in seen:
            seen.add(i_node)
            queue.append(i_node)