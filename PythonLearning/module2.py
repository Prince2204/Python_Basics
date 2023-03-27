#range, in, enumarate, zip,
#random   : randint, shuffle
#input
#list comprehension
#generator
#iterator



# Function that can take in a player input and assign their marker as 'X' or 'O'. 



while game_on:
        if turn =="Player 1":
            # do sometig
            display_board(game_board)
            position=player_choice(game_board)
            place_marker(game_board, player1_marker, position)
            if win_check(game_board,player1_marker):
                print("Congratulations !!! "+turn+" you have won the match....")
                game_on=False
            else:
                if full_board_check(game_board):
                    print(" Board Full, Match is drawn")
                    game_on:False
                    #break
                else:
                    turn="Player 2"

        else:
            # do something
        
        
        # Player2's turn.
            
            #pass







