#Tic-Tac-Toe game python source code
from random import randrange

#Display the board

def display_board(board):
     print("--------" * 3,"-", sep="")
     for row in range(3):
          print("|       " * 3,"|", sep="")
          for col in range(3):
               print("|   " + str(board[row][col]) + "   ", end="")
          print("|")
          print("|       "* 3,"|",sep="")
          print("--------"*3,"-",sep="")

"""user input a number from 1-9,they want to place their 'O' on the board.  checks whether the input is valid, and if the chosen cell is unoccupied, it updates the board with the 'O' at the selected position."""

def enter_move(board):
    valid = False	# fake assumption - we need it to enter the loop
    while not valid:
        move = input("Enter your move: ")
        valid=len(move)==1 and '1'<=move<='9'
        if not valid:
             print("Bad move - repeat your input!")
             continue
        move=int(move)-1#cells number frim 0-8
        row=move//3  #rows
        col=move%3   #columns
        check=board[row][col]  #checks the selected square
        valid=check not in['0','X']
        if not valid:
             print("Field already occupied - repeat your input!")
             continue
        board[row][col]='0'  #set '0' at the selected square


# list of tuples representing the coordinates of unoccupied cells on the board.

def list_of_free_cells(board):
    free=[] #list is empty intially
    for row in range(3):#iterative through rows
        for col in range(3):#iterative through columns
            if board[row][col] not in['0','X']:  #cells are free or not
                free.append((row,col))  #yes it is free. now new tiple added to the list
    return free

#check if a player has won. It checks rows, columns, and diagonals for the specified player's symbol ('X' or 'O'). It returns 'you' if the human player wins ('O'), 'me' if the computer player wins ('X'), and None if there's no winner yet.
def check_win(board,play):
    if play=='X':
        player='me'
    elif play=='0':
        player='you'
    else:
        player=None
    d1=d2=True  #for diagnolas
    for i in range(3):
        if board[i][0]==play and board[i][1]==play and board[i][2]==play:#checks row wise
            return player
        if board[0][i]==play and board[1][i]==play and board[2][i]==play:#checks column wise
            return player
        #if board[i][i]!=play and board[2-i][2-i]!=play:#checks diagnolas d1,d2
            #d1=d2=False
        if board[i][i]!=play:
             d1=False
        if board[i][2-i]!=play:
             d2=False
    if d1 or d2:
         return player
    return None  #there is no winner yet

#handle the computer player's move. It chooses a random unoccupied cell and places an 'X' on the board
def draw_move(board):
    free=list_of_free_cells(board) #make a list of free cells
    cell=len(free)
    if cell>0: #if the list is not empty,choose a place for 'X' and set it
        this=randrange(cell)
        row, col=free[this]
        board[row][col]='X'

board=[[3*j+i+1 for i in range(3)] for j in range(3)]#make an empty board
board[1][1]='X' #set first element in the middle
free=list_of_free_cells(board)
human_turn=True #which turn is it now
win=None #initialize the win variable
while len(free):
     display_board(board)
     if human_turn:
          enter_move(board)
          win=check_win(board,'0')
     else:
          draw_move(board)
          win=check_win(board,'X')
     if win is not None:
          break
     human_turn= not human_turn
     free=list_of_free_cells(board)

display_board(board)
if win== 'you':
    print("You won!")
elif win == 'me':
    print("I won")
else:
    print("Tie!")
    
        
