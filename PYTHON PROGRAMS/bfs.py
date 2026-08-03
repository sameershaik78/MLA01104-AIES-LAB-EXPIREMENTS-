from collections import deque

# Create graph
graph = {}

# Input 1: Number of edges
n = int(input("Enter number of edges: "))

print("Enter each edge (Source Destination):")

# Input 2: Edges
for i in range(n):
    u, v = input().split()

    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []

    graph[u].append(v)
    graph[v].append(u)   # Remove this line for directed graph

# Input 3: Start node
start = input("Enter start node: ")

# Input 4: Goal node
goal = input("Enter goal node: ")


# BFS Function
def bfs(graph, start, goal):
    visited = set()
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)

            for neighbour in graph[node]:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

    return None


# Call BFS
path = bfs(graph, start, goal)

if path:
    print("Path Found:")
    print(" -> ".join(path))
else:
    print("No Path Found")