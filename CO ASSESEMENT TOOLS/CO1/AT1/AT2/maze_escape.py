from collections import deque

maze = [
    ['S', '.', '.', '#', '.'],
    ['#', '#', '.', '#', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '#', '#', '#', '.'],
    ['.', '.', '.', 'G', '.']
]

rows = len(maze)
cols = len(maze[0])

for i in range(rows):
    for j in range(cols):
        if maze[i][j] == 'S':
            start = (i, j)
        if maze[i][j] == 'G':
            goal = (i, j)

directions = [(0,1),(1,0),(0,-1),(-1,0)]

queue = deque([(start,0)])
visited = set()

while queue:
    (x,y),steps = queue.popleft()

    if (x,y)==goal:
        print("Goal Reached!")
        print("Shortest Steps =",steps)
        break

    if (x,y) in visited:
        continue

    visited.add((x,y))

    for dx,dy in directions:
        nx,ny=x+dx,y+dy

        if 0<=nx<rows and 0<=ny<cols:
            if maze[nx][ny]!="#" and (nx,ny) not in visited:
                queue.append(((nx,ny),steps+1))