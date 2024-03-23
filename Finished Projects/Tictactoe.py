import os
import random

#------------------------------------------------------------
#This is a function that displays the board to the user
def display_board(pos):

    os.system('clear')

    print('This is the current state of the game board!\n')
    print(pos[7]+'|',pos[8]+'|',pos[9])
    print('------')
    print(pos[4]+'|',pos[5]+'|',pos[6])
    print('------')
    print(pos[1]+'|',pos[2]+'|',pos[3]+'\n')


#------------------------------------------------------------
#This is a function that assigns either X or O to both players
    
def choose_marker():
    
    os.system('clear')

    marker=('')

    while not (marker== 'x' or marker== 'o'):
        marker = input('To begin the game Player 1 must choose between X or O').lower()
    
    player1 = marker
   
    if marker == 'x':
        return ('x','o')
    else:
        return ('o','x')

#------------------------------------------------------------
#This is a function which takes a marker assigned by the player in another function and assigns it on the board

def player_input(board,marker,position):

    board[position]=marker

#------------------------------------------------------------
#This is a function to check if there is a winner
    
def win_check(board,mark):

    return ((board[1] == mark and board[2] == mark and board[3] == mark) or #Horizontal 1
    (board[4] == mark and board[5] == mark and board[6] == mark) or        #Horizontal 2
    (board[7] == mark and board[8] == mark and board[9] == mark) or        #Horizontal 3
    (board[1] == mark and board[4] == mark and board[7] == mark) or        #Vertical 1
    (board[2] == mark and board[5] == mark and board[8] == mark) or        #Vertical 2
    (board[3] == mark and board[6] == mark and board[9] == mark) or        #Vertical 3
    (board[1] == mark and board[5] == mark and board[9] == mark) or        #Diagonal 1
    (board[3] == mark and board[5] == mark and board[7] == mark))          #Diagonal 2

#------------------------------------------------------------
#This is a function that randomizes which players goes first

def choose_first_player():
    
    flip = random.randint(0,1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'
    
#------------------------------------------------------------
#This is a function that checks if a spot on the board is available
    
def space_check(board, position):

    return board[position] == ' '

#------------------------------------------------------------
#This is a function that checks if the board is full

def full_check(board):

    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

#------------------------------------------------------------
#This is a function that asks a player for their next move

def player_choice(board):
    
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position on the board: (1-9)'))
    
    return position

#------------------------------------------------------------
#This is a function that asks a player if they want to play again

def replay():
    
    choice=('')
    
    while not (choice== 'y' or choice== 'n'):
        choice = input("Do you want to play another game? Y or N").lower()
    if choice == 'y':
        return True
    else:
        return False
#------------------------------------------------------------
#GAME STARTS HERE

os.system('clear')
input('Welcome to Tic Tac Toe! Press any key and hit ENTER to continue.')

while True:
    
    game_on = True                                  #Is there an active game?
    game_board = [' ']*10                           #Setting the initial gameboard
    player1_marker,player2_marker=choose_marker()   #Assignin markers to players
    turn = choose_first_player()                    #Randomizing which player  goes first

    print(turn + ' will go first!')

    while game_on == True:

        if turn == 'Player 1':

            display_board(game_board)                           #Showing the board to the player
            print("Player 2, it's your turn!")
            position = player_choice(game_board)                #Player picks a position on the board
            player_input(game_board,player1_marker,position)    #Player's marker is assigned to the chosen position
        
            if win_check(game_board,player1_marker):            #Checking if Player1 has won
                display_board(game_board)
                print("Player 1 has won the game!")
                game_on = False
            else:
                if full_check(game_board):                      #Checking if there is a tie
                    display_board(game_board)
                    print("The game's result is a tie.")
                    game_on = False
                else:
                    turn = 'Player 2'                           #Player 2's turn
        else:
            
            display_board(game_board)
            print("Player 2, it's your turn!")
            position = player_choice(game_board)
            player_input(game_board,player2_marker,position)

            if win_check(game_board,player2_marker):
                display_board(game_board)
                print("player 2 has won the game!")
                game_on = False
            else:
                if full_check(game_board):
                    display_board(game_board)
                    print("The game's result is a tie.")
                    game_on = False
                else:
                    turn = 'Player 1'
    if not replay():
        ("Thanks for playing Tic Tac Toe! :D")
        break
#The game ends here