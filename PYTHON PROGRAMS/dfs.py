# Depth First Search (DFS)

# Create graph
graph = {}

# Input 1: Number of edges
n = int(input("Enter number of edges: "))

print("Enter each edge (Source Destination):")

# Input 2: Enter edges
for i in range(n):
    u = input("Enter source: ")
    v = input("Enter destination: ")

    if u not in graph:
        graph[u] = []

    if v not in graph:
        graph[v] = []

    graph[u].append(v)
    graph[v].append(u)   # Remove for directed graph


# Input 3: Starting node
start = input("Enter start node: ")

# Input 4: Goal node
goal = input("Enter goal node: ")


# DFS Function
def dfs(graph, start, goal, visited=None, path=None):

    if visited is None:
        visited = set()

    if path is None:
        path = []

    visited.add(start)
    path.append(start)

    # Goal found
    if start == goal:
        return path

    # Visit neighbours
    for neighbour in graph[start]:
        if neighbour not in visited:
            result = dfs(graph, neighbour, goal, visited, path)

            if result:
                return result

    path.pop()
    return None


# Calling DFS
result = dfs(graph, start, goal)


if result:
    print("\nPath Found:")
    print(" -> ".join(result))
else:
    print("\nNo Path Found")