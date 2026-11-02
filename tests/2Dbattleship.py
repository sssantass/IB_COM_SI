import random

# emtpy board
board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

print(board)
print("\nWelcome to Battleship!\n")
player = 0
hits = [0, 0]
misses = [0, 0]

# ships created randomly
for i in range(2):
    while True:
        row = random.randint(0, 4)
        col = random.randint(0, 9)
        if board[row][col] == 0:
            board[row][col] = 1
            break

print(board)

# main game loop 
while True:
    # player input for position chosen
    hitr = int(input("\nEnter row (0-4): "))
    hitc = int(input("Enter column (0-9): "))

    # if the position chosen is a hit, miss or already hit
    if board[hitr][hitc] == 1:
        print("Hit!")
        hits[player] += 1
        board[hitr][hitc] = 2
        if player == 0:
            print("Player 1's turn")
        else:
            print("Player 2's turn")
    elif board[hitr][hitc] == 2:
        print("Boat is already hit!")
        misses[player] += 1
        if player == 0:
            print("Player 1's turn")
        else:
            print("Player 2's turn")
    else:
        print("Miss!")
        misses[player] += 1
        if player == 0:
            print("Player 1's turn")
        else:
            print("Player 2's turn")
    if player == 0:
        player = 1
    else:
        player = 0

    # game over condition if all 5 ships are hit
    if hits[0] + hits[1] == 5:
        print("\nGame Over!")
        print(f"Player 1 hits: {hits[0]}, misses: {misses[0]}")
        print(f"Player 2 hits: {hits[1]}, misses: {misses[1]}")
        break