#tic tac toe game

# Function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, 
#so you get a 3 by 3 board representation.
#from IPython.display import clear_output
def display_board(board):
    print(board[7]+"|"+board[8]+"|"+board[9])
    print("-----")
    print(board[4]+"|"+board[5]+"|"+board[6])
    print("-----")
    print(board[1]+"|"+board[2]+"|"+board[3])

# Function that can take in a player input and assign their marker as 'X' or 'O'. 
# Think about using while loops to continually ask until you get a correct answer.
def player_input():
    marker=""
    while not (marker=='X' or marker=='O'):
        marker=input("Player 1, which marker you will choose: 'X' or 'O' ? : ").upper()
    
    #returning the tuple containing player 1 marker and player 2 marker
    if marker=='X':
        return ('X','O')
    else:
        return ('O','X')
    

# function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.
def place_marker(board, marker, position):
    board[position]=marker

# Function that returns a boolean indicating whether a space on the board is freely available.
def space_check(board, position):
    if board[position]==" ":
        return True
    else:
        print("Position "+str(position)+ " is not free.")
        return False

# function that takes in a board and checks to see if someone has won.
def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

# Function that uses the random module to randomly decide which player goes first. 
# You may want to lookup random.randint() Return a string of which player went first.
import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

# function that checks if the board is full and returns a boolean value. True if full, False otherwise.
def full_board_check(board):
    if " " in board:
        return False
    else:
        return True

# function that asks for a player's next position (as a number 1-9), then uses the function from step 6 to check 
# if it's a free position. If it is, then return the position for later use.
def player_choice(board,turn):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input(turn + ", Choose a position between 1 to 9 to place your marker: "))
    
    return position

# function that asks the player if they want to play again and returns a boolean True if they do want to play again.
def replay():    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


#Function to play tic tac toe game
def common_steps(current_turn,marker,game_on):
     # do something
     turn=""
     #get the position to place the marker on board
     position=player_choice(game_board,current_turn)
     #place the marker on board
     place_marker(game_board, marker, position)
     #display board
     display_board(game_board)
     #Check if player won??
     if win_check(game_board,marker):
         print("Congratulations !!! "+current_turn+" you have won the match....")
         game_on=False
     else:
         #Check if full board
         if full_board_check(game_board):
             print(" Board Full, Match is drawn")
             game_on:False
             #break
         else:
             if current_turn == "Player 1":
                 turn="Player 2"
             else:
                 turn="Player 1"

     return (game_on,turn)

#Use while loops and the functions you've made to run the game!
print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here
    game_board=[" "]*10
    #display_board(game_board)
    player1_marker,player2_marker=player_input()
    turn=choose_first()
    print(turn + " will play the first move")

    play_game=input('Are you ready to play? Enter Yes or No.: ')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            game_on,turn=common_steps(turn,player1_marker,game_on)
        else:
            game_on,turn=common_steps(turn,player2_marker,game_on)


    if not replay():
        break

   
    



