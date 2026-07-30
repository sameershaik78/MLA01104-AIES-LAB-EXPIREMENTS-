ROWS=6
COLS=7

board=[["."]*COLS for _ in range(ROWS)]

def drop(col,player):

    for r in range(ROWS-1,-1,-1):

        if board[r][col]==".":
            board[r][col]=player
            return

moves=[3,3,2,2,1,1,0]

for m in moves:
    drop(m,"X")

for row in board:
    print(" ".join(row))

print("\nPlayer X Wins!")