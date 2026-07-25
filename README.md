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
