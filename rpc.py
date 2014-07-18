__author__ = "Shmuli Bloom"


# import modules that allows for user input to be hidden when being typed

try:
    import msvcrt
except ImportError:
    pass
from getpass import getpass as gp

#Introduce the game to the players

print 'This is a text based game of Rock, Paper, Scissors. Enjoy!'

#find out players' names
name1 = raw_input("What is one of the players' names?")
name2 = raw_input("What is the other player's name?")
prompt_msg = '{}, what is your move?'
invalid_msg = '{}, that is not a valid move. Please try again.'
win_msg = '{} wins!'
valid_moves = ['rock', 'paper', 'scissors', ]


def get_move_for_player(name):
    move = gp(prompt_msg.format(name)).lower()
    while not move in valid_moves:
        print invalid_msg.format(name)
        move = gp(prompt_msg.format(name)).lower()
    return move

#set up 'play again' option
answer = 'yes'
while answer == 'yes':

    move1 = get_move_for_player(name1)
    move2 = get_move_for_player(name2)

    #determine the result and print for players

    if move1 == move2:
        print '{} and {} have tied'.format(name1, name2)

    elif move1 == 'scissors' and move2 == 'paper':
        print win_msg.format(name1)

    elif move2 == 'scissors' and move1 == 'paper':
        print  win_msg.format(name2)

    elif move1 == 'rock' and move2 == 'scissors':
        print  win_msg.format(name1)

    elif move2 == 'rock' and move1 == 'scissors':
        print  win_msg.format(name2)

    elif move1 == 'paper' and move2 == 'rock':
        print  win_msg.format(name1)

    else:
        print  win_msg.format(name2)

    #print players moves so they can see that the outcome was correctly decided

    print "{}'s move was {} and {}'s move was {}.".format(name1, move1, name2, move2)


    #give the players the option to play again

    answer = raw_input(
        'Do you want to play again? Answer, yes or no (any other response will end the game by default).').lower()



    # work on play again option, including an 'are you sure' secondary prompt

    # confirm the players option to play again

##    #x = 'no'
##    while x == 'no':
##         x = raw_input('\n' + 'Are you sure? Answer yes or no.)
##        answer = raw_input('\n' + 'Do you want to play again? Answer, yes or no (any other response will end the game).').lower()
##       
##                  

