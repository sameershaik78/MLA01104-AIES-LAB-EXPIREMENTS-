# Crypt Arithmetic Problem

from itertools import permutations

letters = ('S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y')

# Only one input
choice = input("Enter YES to solve: ")

if choice.upper() == "YES":

    for p in permutations(range(10), 8):

        S, E, N, D, M, O, R, Y = p

        # Leading digit cannot be zero
        if S == 0 or M == 0:
            continue

        SEND = 1000*S + 100*E + 10*N + D
        MORE = 1000*M + 100*O + 10*R + E
        MONEY = 10000*M + 1000*O + 100*N + 10*E + Y

        if SEND + MORE == MONEY:
            print("Solution Found")
            print("SEND =", SEND)
            print("MORE =", MORE)
            print("MONEY =", MONEY)
            break

else:
    print("Program Stopped")