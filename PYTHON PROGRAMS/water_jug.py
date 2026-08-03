from collections import deque

def water_jug():
    visited = set()
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))
        print((x, y))

        if x == 2:
            print("Goal Reached!")
            return

        next_states = [
            (4, y),                         # Fill Jug A
            (x, 3),                         # Fill Jug B
            (0, y),                         # Empty Jug A
            (x, 0),                         # Empty Jug B
            (min(4, x+y), y-(min(4, x+y)-x)),   # Pour B -> A
            (x-(min(3, x+y)-y), min(3, x+y))    # Pour A -> B
        ]

        for state in next_states:
            if state not in visited:
                queue.append(state)

water_jug()