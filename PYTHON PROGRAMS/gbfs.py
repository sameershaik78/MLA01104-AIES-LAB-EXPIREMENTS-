# Greedy Best First Search (GBFS)

from queue import PriorityQueue

# Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

# Heuristic values
heuristic = {
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 3,
    'E': 2,
    'F': 4,
    'G': 0
}

# Goal node
goal = 'G'

# Only one input
start = input("Enter start node: ")

visited = set()
pq = PriorityQueue()
pq.put((heuristic[start], start))

print("Traversal:")

while not pq.empty():
    h, node = pq.get()

    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        if node == goal:
            print("\nGoal Reached!")
            break

        for neighbor in graph[node]:
            if neighbor not in visited:
                pq.put((heuristic[neighbor], neighbor))
else:
    print("\nGoal Not Found!")