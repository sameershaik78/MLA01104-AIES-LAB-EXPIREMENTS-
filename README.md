# MLA01104-AIES-LAB-EXPIREMENTS-
SHAIK SAMEER PASHA 192425383

**1. Breadth First Search (BFS)**
Start
Create Queue
Mark start node as visited
Enqueue start node

While Queue is not empty
    Dequeue a node
    Display node
    For each adjacent node
        If not visited
            Mark visited
            Enqueue node
End While
Stop
**2. Depth First Search (DFS)**
Start
Create Stack
Push start node

While Stack is not empty
    Pop node
    If node not visited
        Mark visited
        Display node
        Push all adjacent nodes
End While
Stop

**3. Uniform Cost Search (UCS)**
Start
Create Priority Queue
Insert start node with cost 0

While Queue is not empty
    Remove node with minimum cost
    If goal reached
        Stop
    Expand neighbors
    Update cost
    Insert into Queue
End While
Stop

****4. A* Search****
Start
Create Priority Queue
Insert start node

While Queue is not empty
    Remove node with lowest f(n)
    If goal reached
        Stop
    Expand neighbors
    Calculate f(n)=g(n)+h(n)
    Insert into Queue
End While
Stop

**5. Greedy Best First Search (GBFS)**
Start
Create Priority Queue
Insert start node

While Queue is not empty
    Remove node with smallest heuristic
    If goal reached
        Stop
    Expand neighbors
    Insert neighbors using heuristic value
End While
Stop

**6. MiniMax Algorithm**
MiniMax(node)

If node is leaf
    Return value

If Maximizer
    Return maximum of child values

Else
    Return minimum of child values
End

**7. Alpha-Beta Pruning**
AlphaBeta(node, alpha, beta)

If node is leaf
    Return value

If Maximizer
    Update alpha
Else
    Update beta

If alpha >= beta
    Prune remaining branches

Return best value

**8. Water Jug Problem**
Start
Fill jug
Empty jug
Pour water from one jug to another
Repeat until target quantity is obtained
Display solution
Stop

**9. N-Queen Problem**
Start
Place queen in first row

For each row
    Check safe position
    Place queen
    Move to next row
    If no position
        Backtrack
End

Display solution
Stop

**10. Crypt Arithmetic**
Start
Assign digits to letters
Check leading digit is not zero
Verify arithmetic equation
If valid
    Display solution
Else
    Try another assignment


**11. 8-Puzzle Problem**
Start
Place initial state in Queue

While goal not reached
    Remove current state
    Generate possible moves
    Add new states
End While

Display solution path
Stop

**12. CMD (Monkey and Banana Problem)**
Start
Monkey moves to box
Monkey pushes box under banana
Monkey climbs box
Monkey picks banana
Goal achieved
Stop
