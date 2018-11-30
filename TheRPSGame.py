import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


# the Base Class Player AS main / guidance Class
# To be Extended By All Player Types


class Player:
    scores = 0

    # abstracted Or Pass method pre defined Move & Learn
    # Of Each Player To be Implemented / Overridden Each As Required

    def move(self):
        pass

    def learn(self, my_move, their_move):
        pass

    # Score is to be called particularly on a player is a winner to _
    # increase his score counter (like setter )
    def score(self):
        self.scores += 1
        return self.scores


# A computer Player Which Always Plays Rock
class ComputerRock(Player):

    # Always Rock Player Move Method Implementation
    def move(self):
        return "rock"


# A Computer Player Of Random Selection with saving Of _
# his moves And Others moves Also
class ComputerRandom(Player):
    my_moves = []
    other_moves = []

    def move(self):
        return random.choice(moves)


# A Computer Player Which Always Reflect The Human Previous Move_
#   with saving Of his moves And Others moves Also
class ComputerReflect(Player):
    my_moves = []
    other_moves = []
    counter = 0

    def move(self):
        if self.counter == 0:
            self.counter += 1
            move = random.choice(moves)
        else:
            move = self.other_moves[self.counter - 1]
            self.counter += 1
        return move

    def learn(self, my_move, their_move):
        self.my_moves.append(my_move)
        self.other_moves.append(their_move)


# A Computer Player Of Random Selection But never _
# Repeated in 3 rounds selection
# with saving Of his moves (in My_moves ARR & all_myMoves Also )_
#  And Others moves Also
class ComputerCycle(Player):
    my_moves = []
    other_moves = []
    counter = 0

    def move(self):

        if self.counter % 3 == 0:
            self.counter += 1
            move = 'rock'
        elif self.counter % 3 == 1:
            move = 'paper'
            self.counter += 1
        elif self.counter % 3 == 2:
            move = 'scissors'
            self.counter += 1
        return move

    def learn(self, my_move, their_move):
        self.my_moves.append(my_move)
        self.other_moves.append(their_move)


# beats rolls of the game Outer function
def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


# A Human Player Class Extends / inherit Main Player Class _
# With His Additional Properties / Methods
class HumanPlayer(Player):

    def move(self):
        u_input_move = input("Please Choose ( rock , paper , scissors )>>>)")
        while u_input_move not in ["rock", "paper", "scissors"]:
            u_input_move = input("Please Choose ( rock , paper ," +
                                 " scissors >>>)").lower()
        return u_input_move

    def game_rounds(self):
        u_input_round = input("Please Choose ( 1 or 3 or 5 or 7 or 9 ) \n" +
                              "(or any ODD number As Num. Of Rounds To Play)" +
                              ">>>)")
        while u_input_round not in ["1", "3", "5", "7", "9"]:
            print("should be Valid and Odd Number ")
            u_input_round = input("Please Choose(1 or 3 or 7 or 9)\n(or " +
                                  "any ODD number As Num. Of Rounds To Play" +
                                  ")>>>)")
        return int(u_input_round)


# the Game Manager Class Has-A Class Relation
class Game:

    # Constructor Of Two Player Types
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"You: {move1}  Computer : {move2}")  # Printing Each Player Move
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        # Checking who won the Round To Call His Score Incrementer _
        # Method And Print the new Score
        if move1 == move2:
            print(f" Tie Round No Winner >> Computer : {self.p1.scores} " +
                  f"& You : {self.p2.scores}")
        elif beats(move1, move2):
            self.p1.score()
            print(f" Computer 1 Won this Round || \n Score Is || Computer " +
                  f": {self.p1.scores} & You  : {self.p2.scores}")
        else:
            self.p2.score()
            print(f" You Won This Round Keep Up \n Score Is || Computer : " +
                  f"{self.p1.scores} & You  : {self.p2.scores}")

    # Game Starter Which Determine and recall Rounds count
    def play_game(self):
        print("Game start!")
        rounds = self.p2.game_rounds()
        print(f"A Game Of {rounds} Rounds Started >>>>>")
        for round_no in range(rounds):
            print(f"Round {round_no+1}:")
            self.play_round()
        if self.p1.scores > self.p2.scores:
            print(f"Computer  : won Score is : {self.p1.scores} rounds To :" +
                  f" {self.p2.scores} good game  ")
        elif self.p1.scores < self.p2.scores:
            print(f" You : won Score is : {self.p2.scores} rounds To : " +
                  f"{self.p1.scores}  good game  ")
        else:
            print(f"Game Has No Winner Score is : {self.p2.scores} rounds " +
                  f"To :{self.p1.scores}  Tie  game  ")
        print("Game Finished  Now !")


if __name__ == '__main__':
    #  input To determine a computer player Type And Create Obj. _
    # from a certain Type of the 4 Classes Created
    u_input = input(
        "Please Choose Computer Player Mode \n( A , B , C , D ) " +
        "Sorted From Easy To harder Mode >>>)").upper()
    while u_input not in ["A", "B", "C", "D"]:
        u_input = input(
                        "Please Choose Computer Player Mode \n(A,B,C,D) " +
                        "Sorted From Easy To harder Mode >>>)").upper()

    if u_input == "A":
        game = Game(ComputerRock(), HumanPlayer())
    elif u_input == "B":
        game = Game(ComputerReflect(), HumanPlayer())
    elif u_input == "C":
        game = Game(ComputerRandom(), HumanPlayer())
    else:
        game = Game(ComputerCycle(), HumanPlayer())
    game.play_game()
