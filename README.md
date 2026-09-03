# MLA01104-AIES-LAB-EXPIREMENTS-
SHAIK SAMEER PASHA 192425383
                                 **PYTHON PROGRAMS PSECUDO CODES**

**1. Breadth First Search (BFS)**
BFS(Graph, Start)

Start
Create an empty Queue
Mark Start as Visited
Enqueue Start into Queue

While Queue is not empty
    Node ← Dequeue from Queue
    Display Node

    For each adjacent node of Node
        If adjacent node is not visited
            Mark adjacent node as Visited
            Enqueue adjacent node into Queue
        End If
    End For
End While

Stop

**2 DEPTH FIRST SEARCH (DFS)**
DFS(Graph, Start)

Start
Create an empty Stack
Push Start into Stack

While Stack is not empty
    Node ← Pop from Stack

    If Node is not visited
        Mark Node as Visited
        Display Node

        For each adjacent node of Node
            If adjacent node is not visited
                Push adjacent node into Stack
            End If
        End For
    End If
End While

Stop
**3 UNIFORM COST SEARCH (UCS)**
UCS(Graph, Start, Goal)

Start
Create a Priority Queue
Insert Start into Priority Queue with Cost = 0

While Priority Queue is not empty
    Node ← Remove node with minimum Cost

    If Node is Goal
        Display solution
        Stop
    End If

    For each neighbor of Node
        NewCost ← Cost(Node) + EdgeCost(Node, Neighbor)

        If Neighbor is not visited
           OR NewCost < previously known cost
            Update cost of Neighbor
            Insert Neighbor into Priority Queue
        End If
    End For
End While

Stop

**4 A* SEARCH**
A_Star(Graph, Start, Goal)

Start
Create a Priority Queue
Set g(Start) = 0
Calculate f(Start) = g(Start) + h(Start)
Insert Start into Priority Queue

While Priority Queue is not empty
    Node ← Remove node with lowest f(Node)

    If Node is Goal
        Display solution
        Stop
    End If

    For each neighbor of Node
        Calculate new g-cost

        If new g-cost is better than previous g-cost
            g(Neighbor) ← new g-cost
            f(Neighbor) ← g(Neighbor) + h(Neighbor)
            Insert Neighbor into Priority Queue
        End If
    End For
End While

Stop

**5 GREEDY BEST FIRST SEARCH(GBFS)**
GBFS(Graph, Start, Goal)

Start
Create a Priority Queue
Insert Start using heuristic h(Start)

While Priority Queue is not empty
    Node ← Remove node with smallest h(Node)

    If Node is Goal
        Display solution
        Stop
    End If

    Mark Node as Visited

    For each neighbor of Node
        If neighbor is not visited
            Insert neighbor into Priority Queue
            Priority ← h(Neighbor)
        End If
    End For
End While

Stop
**6 MINMAX ALGORITHM **
MINIMAX(Node, Depth, MaximizingPlayer)

If Node is a terminal node
    Return UtilityValue(Node)
End If

If MaximizingPlayer = TRUE
    BestValue ← -∞

    For each child of Node
        Value ← MINIMAX(child, Depth + 1, FALSE)
        BestValue ← MAX(BestValue, Value)
    End For

    Return BestValue

Else
    BestValue ← +∞

    For each child of Node
        Value ← MINIMAX(child, Depth + 1, TRUE)
        BestValue ← MIN(BestValue, Value)
    End For

    Return BestValue
End If

**7 ALPHA BETA PRUNING **
ALPHA_BETA(Node, Alpha, Beta, MaximizingPlayer)

If Node is a terminal node
    Return UtilityValue(Node)
End If

If MaximizingPlayer = TRUE

    BestValue ← -∞

    For each child of Node
        Value ← ALPHA_BETA(child, Alpha, Beta, FALSE)

        BestValue ← MAX(BestValue, Value)
        Alpha ← MAX(Alpha, BestValue)

        If Alpha ≥ Beta
            Prune remaining branches
            Break
        End If
    End For

    Return BestValue

Else

    BestValue ← +∞

    For each child of Node
        Value ← ALPHA_BETA(child, Alpha, Beta, TRUE)

        BestValue ← MIN(BestValue, Value)
        Beta ← MIN(Beta, BestValue)

        If Alpha ≥ Beta
            Prune remaining branches
            Break
        End If
    End For

    Return BestValue
End If
**8 WATER JUG PROBLEM**
WATER_JUG(A, B, T)

Start
Create a Queue
Insert initial state (0, 0)
Mark initial state as Visited

While Queue is not empty

    CurrentState ← Dequeue

    If CurrentState contains target quantity T
        Display solution path
        Stop
    End If

    Generate possible states:
        1. Fill Jug A
        2. Fill Jug B
        3. Empty Jug A
        4. Empty Jug B
        5. Pour Jug A into Jug B
        6. Pour Jug B into Jug A

    For each new state
        If new state is not visited
            Mark new state as Visited
            Enqueue new state
        End If
    End For

End While

Display "No solution"
Stop
**9 N QUEEN PROBLEM**
N_QUEEN(Row)

If Row > N
    Display solution
    Return TRUE
End If

For Column ← 1 to N

    If Position(Row, Column) is Safe

        Place Queen at (Row, Column)

        If N_QUEEN(Row + 1) = TRUE
            Return TRUE
        End If

        Remove Queen from (Row, Column)
    End If

End For

Return FALSE
**10 Cryptarithmetic Problem**
CRYPTARITHMETIC(Words, Result)

Start

Identify all unique letters
Assign a different digit (0–9) to each letter

For each possible digit assignment

    Ensure leading letters are not assigned 0

    Replace letters with their assigned digits

    Evaluate the arithmetic equation

    If equation is correct
        Display letter-to-digit assignment
        Display solution
        Stop
    End If

End For

Display "No solution"
Stop

**11 8 PUZZLE PROBLEM**
8_PUZZLE(Start, Goal)

Start
Create a Queue
Insert Start state into Queue
Mark Start as Visited
Store parent of Start as NULL

While Queue is not empty

    Current ← Dequeue from Queue

    If Current = Goal
        Display solution path
        Stop
    End If

    Generate all possible moves:
        Move blank Up
        Move blank Down
        Move blank Left
        Move blank Right

    For each NewState

        If NewState is valid
           AND NewState is not visited

            Mark NewState as Visited
            Store Current as parent of NewState
            Enqueue NewState
        End If

    End For

End While

Display "No solution"
Stop
**12 MONKEY AND BANANA PROBLEM **
MONKEY_BANANA()

Start

Initial state:
    Monkey is on floor
    Box is away from banana
    Banana is hanging above

If monkey is not near the box
    Monkey moves to the box
End If

If box is not under the banana
    Monkey pushes box under the banana
End If

Monkey climbs onto the box

If monkey is on the box
    Monkey reaches for the banana
    Monkey picks the banana
End If

If banana is obtained
    Display "Goal Achieved"
Else
    Continue searching
End If

Stop
