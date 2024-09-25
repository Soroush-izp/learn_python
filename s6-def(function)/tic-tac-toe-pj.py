from termcolor import colored
board = list(range(1, 10))
winners = ( # all state player can win
    (0, 1, 2),  # Top row  
    (3, 4, 5),  # Middle row  
    (6, 7, 8),  # Bottom row  
    (0, 3, 6),  # Left column  
    (1, 4, 7),  # Middle column  
    (2, 5, 8),  # Right column  
    (0, 4, 8),  # Diagonal from top left to bottom right  
    (2, 4, 6)   # Diagonal from top right to bottom left 
)
moves = (   # section Priority, computer have to first signing(base on priority) specified
    (1, 3, 7, 9), # sides
    (5,), # center # if i don't put comma , end of that don't process it as Tuple
    (2, 4, 6, 8)
)

def print_board():
    j = 1
    for i in board:
        end = " "
        if j % 3 == 0:
            end = '\n\n'
        if i == 'P':
            print(colored(f"[{i}]", 'blue'), end=end)
        elif i == 'C':
            print(colored(f"[{i}]", 'yellow'), end=end)
        else:
            print(f"[{i}]", end=end)
        j += 1


def has_empty_space():
    return board.count("P") + board.count("C") != 9


def computer_move():
    mv = -1
    # check if computer can win
    for i in range(1, 10):
        if make_move(board, computer, i, True)[1]:
            mv = i
            break
    # check if player can win (preventing him)
    if mv == -1:
        for j in range(1, 10):
            if make_move(board, player, j, True)[1]:
                mv = j
                break
    # just move
    if mv == -1:
        for tup in moves:
            for f in tup:
                if mv == -1 and can_move(board, f):
                    mv = f
                    break
    return make_move(board, computer, mv)


def make_move(brd, plyr, mve, undo=False):
    if can_move(brd, mve):
        brd[mve-1] = plyr
        win = is_winner(brd, plyr)
        if undo:
            brd[mve-1] = mve
        return True, win
    return False, False


def is_winner(brd, plyr):
    win = True
    for tup in winners:
        win = True 
        for j in tup:
            if brd[j] != plyr:
                win = False
                break
        if win:
            break
    return win
    
def can_move(brd, mve):
    if mve in range(1, 10) and isinstance(brd[mve-1], int):
        return True
    return False


player, computer = "P", "C"
print(f"Player: {player} \nComputer: {computer}\n")
while has_empty_space():
    print_board()
    move = int(input("Choose your move(1-9): "))
    moved, won = make_move(board, player, move)
    if not moved:
        print("Invalid number! Try again!")
        continue
    if won:
        print(colored("You won:)", 'green'), end='\n\n')
        break
    elif computer_move()[1]:
        print(colored("Computer won, You lose:(", 'red'), end='\n\n')
        break

print_board()
