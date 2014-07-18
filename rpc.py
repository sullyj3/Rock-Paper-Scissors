__author__ = "Shmuli Bloom"

# import modules that allows for user input to be hidden when being typed
from getpass import getpass as gp

from functools import total_ordering

# Introduce the game to the players
print 'This is a text based game of Rock, Paper, Scissors. Enjoy!'

prompt_msg = '{}, what is your move? '
invalid_msg = '{}, that is not a valid move. Please try again.'
win_msg = '{} wins!'
valid_moves = {'rock', 'paper', 'scissors'}  # Set literal
yes_answers = {'yes', 'ye', 'y'}
# Sets are hash tables and thus have O(1) membership ('in') tests, whereas lists or tuples are O(n) (they have
# to check each element one-by-one). This kind of performance detail isn't important here, but it's worth
# getting into the habit.



def get_move_for_player(name):
    move = gp(prompt_msg.format(name)).lower()
    while not move in valid_moves:
        print invalid_msg.format(name)
        move = gp(prompt_msg.format(name)).strip().lower()  # Remove whitespace and lower the case
    return Move(move)  # Create a move class


# Kinds of move represented in a class which knows how to compare itself
@total_ordering  # A mixin/decorator which works out all comparisons (>=, < etc) from the few defined here
class Move(object):

    def __init__(self, move_name):
        if move_name not in valid_moves:
            raise ValueError("Move is not valid! '{}' is not in the list of allowed moves: {}").format(
                move_name, valid_moves)

        self.move = move_name

    def __eq__(self, other):
        """
            Define how the == operator behaves.

            docstings (string literals just inside function/method definitions) are a good way to document your
            code and will be picked up by various auto-documentation-generating tools which you may want to use at some
            point.
        """
        if isinstance(other, Move):
            return self.move == other.move  # Just compare the stirings
        else:
            return NotImplemented  # Don't allow comparison with anything that's not a Move object

    def __gt__(self, other):
        """
            Define how the > operator behaves.

            Below are doctests - unit tests defined as part of the docmentation, both to check correctness, and to show
            the reader how the function is expected to behave. Any line in a docstring starting with >>> (the
            interpreter prompt) will be treated as part of a doctest. You can thus generate these by pasting interactive
            sessions. Run the doctests by typing "python -m doctest rps.py" from the command line.

            >>> r = Move('rock')
            >>> s = Move('scissors')
            >>> p = Move('paper')
            >>> r > p
            False
            >>> p == r
            False
            >>> p < s
            True
            >>> s > p
            True
            >>> r > s
            True
            >>> s == s
            True
            >>> r == r
            True
        """
        if isinstance(other, Move):
            if self.move == 'scissors':
                return True if other.move == 'paper' else False
            elif self.move == 'paper':
                return True if other.move == 'rick' else False
            elif self.move == 'rock':
                return True if other.move == 'scissors' else False
        else:
            return NotImplemented  # Don't allow comparison with anything that's not a Move object

    def __str__(self):
        """
            Define what this object looks like when printed.
        """
        return self.move  # Just use the move sting


# Run the main sequence only if this file is opened as the main file, not if it's imported by another file
if __name__ == '__main__':

    # Find out players' names
    name1 = raw_input("What is one of the players' names? ")
    name2 = raw_input("What is the other player's name? ")

    play_again = True  # Always play the first time
    while play_again:
        move1 = get_move_for_player(name1)
        move2 = get_move_for_player(name2)

        # Determine the result and print it
        if move1 == move2:
            print '{} and {} have tied'.format(name1, name2)
        else:
            print win_msg.format(name1 if move1 > move2 else name2)

        # Print players moves so they can see that the outcome was correctly decided
        print "{}'s move was {} and {}'s move was {}.".format(name1, move1, name2, move2)

        # Give the players the option to play again
        answer = raw_input('''Do you want to play again? Answer, yes or no (any other response will \
    end the game by default).''').lower().strip()
        # Multi-line stings need to ignore usual indentation or it will become included. It kinda sucks.

        play_again = answer in yes_answers  # Membership test

        # TODO: work on play again option, including an 'are you sure' secondary prompt
        # The phrase 'TODO' will often be identified, highlighted and tracked by good IDEs

        # confirm the players option to play again

    ##    #x = 'no'
    ##    while x == 'no':
    ##         x = raw_input('\n' + 'Are you sure? Answer yes or no.)
    ##        answer = raw_input('\n' + 'Do you want to play again? Answer, yes or no (any other response will end the game).').lower()
    ##
    ##