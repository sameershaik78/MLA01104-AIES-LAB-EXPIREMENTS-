# MLA01104-AIES-LAB-EXPIREMENTS-
SHAIK SAMEER PASHA 192425383

BFS 1

Algorithm BFS(Graph, Start)

1. Create an empty queue Q.
2. Create an empty list/set Visited.
3. Enqueue(Start) into Q.
4. Mark Start as Visited.

5. While Q is not empty do
      a. Dequeue a node N from Q.
      b. Print N.
      c. For each adjacent node M of N do
            If M is not Visited then
                Mark M as Visited.
                Enqueue(M) into Q.
            End If
         End For
   End While

6. Stop.

BFS 2

Algorithm BFS(Graph, Start)

1. Create an empty Queue Q.
2. Create an empty Visited list.
3. Enqueue(Start) into Q.
4. Mark Start as Visited.

5. While Q is not empty do
      a. Remove first node from Q.
      b. Print the node.
      c. For every adjacent node of the current node
            If the node is not Visited then
                Mark it as Visited.
                Enqueue it into Q.
            End If
         End For
   End While

6. Stop.

N-QUEEN 
Algorithm N_Queen(Board, Row, N)

1. If Row = N
      Print the Board
      Return True

2. For each Column from 0 to N-1
      If position (Row, Column) is safe
            Place Queen at (Row, Column)

            If N_Queen(Board, Row + 1, N) = True
                  Return True

            Remove Queen from (Row, Column)   // Backtrack

3. Return False


Algorithm IsSafe(Board, Row, Column, N)

1. Check the same column in previous rows.
2. Check the upper-left diagonal.
3. Check the upper-right diagonal.
4. If no queen is found in any of the above,
      Return True
   Else
      Return False


Main Algorithm

1. Read the value of N.
2. Create an N × N board and initialize all cells to empty.
3. Call N_Queen(Board, 0, N).
4. If no solution exists,
      Print "No Solution Found".
5. Stop.
   
 8 PUZZLE Using BFS
 Algorithm EightPuzzle(Start, Goal)

1. Create an empty Queue.
2. Create an empty Visited set.
3. Insert the Start state into the Queue.
4. Mark the Start state as Visited.

5. While the Queue is not empty
      a. Remove the front state from the Queue.
      b. If the current state is the Goal state
            Print "Goal Reached"
            Print the solution path
            Stop.
      c. Find the position of the blank tile (0).
      d. Generate all valid next states by moving
         the blank tile Up, Down, Left, or Right.
      e. For each generated state
            If the state is not in Visited
                  Add it to Visited.
                  Insert it into the Queue.

6. Print "No Solution Exists".
7. Stop

8. A*Search
 START

1. Create OPEN list and CLOSED list.
2. Add the start node to the OPEN list.
3. While OPEN list is not empty:
      a. Select the node with the lowest f(n).
      b. If it is the goal node:
            Display the path.
            Stop.
      c. Move the node from OPEN to CLOSED.
      d. For each neighboring node:
            If neighbor is not in CLOSED:
                Calculate:
                    g(n) = cost from start
                    h(n) = heuristic value
                    f(n) = g(n) + h(n)
                Add or update the neighbor in OPEN.
4. If OPEN becomes empty:
      Display "No Path Found".

STOP
