from queue import PriorityQueue

goal = [
    [1,2,3],
    [4,5,6],
    [7,8,0]
]

start = [
    [1,2,3],
    [4,0,6],
    [7,5,8]
]

def heuristic(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count += 1
    return count

pq = PriorityQueue()
pq.put((heuristic(start), start))

visited = []

while not pq.empty():

    cost, current = pq.get()

    print("Current State:")
    for row in current:
        print(row)

    print("Heuristic =", heuristic(current))

    if current == goal:
        print("\nGoal State Reached!")
        break

    visited.append(current)

    # Find blank tile
    for i in range(3):
        for j in range(3):
            if current[i][j] == 0:
                x = i
                y = j

    directions = [
        (-1,0),
        (1,0),
        (0,-1),
        (0,1)
    ]

    for dx,dy in directions:

        nx = x + dx
        ny = y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:

            new_state = [row[:] for row in current]

            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]

            if new_state not in visited:
                pq.put((heuristic(new_state), new_state))