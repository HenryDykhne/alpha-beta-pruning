from re import X
import numpy as np
from TicTacToeState import TicTacToeState
from AI import AI

def ai_battle(currentState):
    print("Strong Computer Plays X, Weak Computer Plays O:")
    ai = AI('3', '2', '2')
    aiWeak = AI('2', '1', '0')
    while ai.game_result(currentState) == None:
        display_board(currentState)
        if currentState.sideToMove == 1:
            print('Strong Computer is thinking.')
            y,x = ai.move(currentState)
            print("Strong Computer plays at: " + str(x) + ", " + str(y))
        else:
            print('Weak Computer is thinking.')
            y,x = aiWeak.move(currentState)
            print("Weak Computer plays at: " + str(x) + ", " + str(y))
        currentState = ai.make_move(currentState, y, x)
    display_board(currentState)
    winner = ai.game_result(currentState)
    if winner == 1:
        print('X Wins')
    elif winner == -1:
        print('O Wins')
    else:
        print('Draw')

def display_board(currentState):
    board = '-'*(2*currentState.sideLength + 1) + '\n'
    for row in currentState.grid:
        board += '|'
        for col in row:
            if col == 1:
                sym = 'X'
            elif col == -1:
                sym = 'O'
            else:
                sym = ' '
            board += str(sym) + '|'
        board += '\n' + '-'*(2*currentState.sideLength + 1) + '\n'
    print(board)

def is_valid_move(currentState, y, x):
    if 0 <= x < currentState.sideLength and 0 <= y < currentState.sideLength and currentState.grid[y][x] == 0:
        return True
    return False

def gen_start_state(sideLength):
    grid = np.zeros((sideLength, sideLength), dtype=int)
    return TicTacToeState(grid, sideLength, 1, sideLength * sideLength)

print("Lets play tic-tac-toe.")
variant = "0"
while variant not in ["1", "2", "3"]:
    variant = input("Select Variant (Type 1, 2 or 3):\n1) 3x3\n2) 4x4\n3) 5x5\n")
variant = int(variant) + 2
if input("Play, or Watch Strong vs weak AI? (Type 1 or 2):\n1) Play\n2) Watch\n") == '2':
    ai_battle(gen_start_state(variant))
    exit()
aiType = "0"
while aiType not in ["1", "2", "3"]:
    aiType = input("Select AI (Type 1, 2 or 3):\n1) random\n2) minimax\n3) alphabeta\n")

utility = "0"
if aiType in ["2", "3"]:
    while utility not in ["1", "2"]:
        utility = input("Select Utility Function (Type 1 or 2):\n1) weak\n2) strong\n")

ordering = "0"
if aiType == "3":
    while ordering not in ["1", "2"]:
        ordering = input("Select Move Ordering Algorithm (Type 1 or 2):\n1) random\n2) order by lower depth eval\n")


currentState = gen_start_state(variant)
ai = AI(aiType, utility, ordering)
print("Human Plays X, Computer Plays O. Lets begin:")
# 1 is X, -1 is O
while ai.game_result(currentState) == None:
    display_board(currentState)
    y,x = -1, -1
    if currentState.sideToMove == 1:
        while not is_valid_move(currentState, y, x):
            print("Select a valid move. (x is left to right, y is top to bottom, top left starts at (0,0))")
            try:
                x = int(input("Enter the x coordinate of your move: "))
                y = int(input("Enter the y coordinate of your move: "))
            except ValueError:
                x = -1
                y = -1
    else:
        print('Computer is thinking.')
        y,x = ai.move(currentState)
        print("Computer plays at: " + str(x) + ", " + str(y))
    currentState = ai.make_move(currentState, y, x)
display_board(currentState)
winner = ai.game_result(currentState)
if winner == 1:
    print('X Wins')
elif winner == -1:
    print('O Wins')
else:
    print('Draw')
print("Good Game. Goodbye.")