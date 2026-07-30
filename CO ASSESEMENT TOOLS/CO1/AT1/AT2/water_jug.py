from collections import deque

capacity=(11,9)
goal=8

visited=set()

queue=deque([((0,0),[])])

while queue:

    (a,b),path=queue.popleft()

    if a==goal or b==goal:
        print("Solution Found")
        print(path+[(a,b)])
        break

    if (a,b) in visited:
        continue

    visited.add((a,b))

    next_states=[]

    next_states.append((capacity[0],b))
    next_states.append((a,capacity[1]))

    next_states.append((0,b))
    next_states.append((a,0))

    transfer=min(a,capacity[1]-b)
    next_states.append((a-transfer,b+transfer))

    transfer=min(b,capacity[0]-a)
    next_states.append((a+transfer,b-transfer))

    for state in next_states:
        if state not in visited:
            queue.append((state,path+[(a,b)]))