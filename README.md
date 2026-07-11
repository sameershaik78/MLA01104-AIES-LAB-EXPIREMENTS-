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
