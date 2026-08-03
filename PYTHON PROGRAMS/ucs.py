# Uniform Cost Search (UCS)

import heapq

# Create graph
graph = {}

# Input 1: Number of edges
n = int(input("Enter number of edges: "))

print("Enter each edge (Source Destination Cost):")

# Enter edges
for i in range(n):
    u, v, cost = input().split()
    cost = int(cost)

    if u not in graph:
        graph[u] = []

    if v not in graph:
        graph[v] = []

    graph[u].append((v, cost))
    graph[v].append((u, cost))


# Fixed Start and Goal nodes
start = "A"
goal = "G"


# UCS Function
def ucs(graph, start, goal):

    queue = [(0, start, [])]

    visited = set()

    while queue:

        cost, node, path = heapq.heappop(queue)

        if node in visited:
            continue

        visited.add(node)

        path = path + [node]

        if node == goal:
            return path, cost

        for neighbour, edge_cost in graph[node]:
            if neighbour not in visited:
                heapq.heappush(
                    queue,
                    (cost + edge_cost, neighbour, path)
                )

    return None, None


# Calling UCS
result, total_cost = ucs(graph, start, goal)


# Output
if result:
    print("\nPath Found:")
    print(" -> ".join(result))
    print("Total Cost:", total_cost)

else:
    print("\nNo Path Found")