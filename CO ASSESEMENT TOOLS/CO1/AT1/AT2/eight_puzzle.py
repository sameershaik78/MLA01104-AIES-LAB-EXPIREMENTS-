from queue import PriorityQueue

goal=(1,2,3,4,5,6,7,8,0)

start=(1,2,3,
       4,0,6,
       7,5,8)

def heuristic(state):
    h=0
    for i in range(9):
        if state[i]!=0 and state[i]!=goal[i]:
            h+=1
    return h

pq=PriorityQueue()

pq.put((heuristic(start),0,start))

visited=set()

while not pq.empty():

    f,g,state=pq.get()

    if state==goal:
        print("Puzzle Solved!")
        print("Moves =",g)
        break

    if state in visited:
        continue

    visited.add(state)

    zero=state.index(0)

    x=zero//3
    y=zero%3

    directions=[(-1,0),(1,0),(0,-1),(0,1)]

    for dx,dy in directions:

        nx=x+dx
        ny=y+dy

        if 0<=nx<3 and 0<=ny<3:

            nz=nx*3+ny

            lst=list(state)

            lst[zero],lst[nz]=lst[nz],lst[zero]

            new_state=tuple(lst)

            if new_state not in visited:

                pq.put((g+1+heuristic(new_state),g+1,new_state))