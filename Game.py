from Player import Player
from Computer import Computer
from Human import Human

class Game:
    def __init__(self):
        self.player_one = Player()
        self.player_two = Player()
        self.computer = Computer()
        self.human = Human()

    def run_game(self):
        self.welcome()
        self.gesture_comparison()

    def welcome(self):
        print('Welcome to RPSLS or better known as Rock, Paper, Scissors, Lizard, Spock.')

    def computer_player(self):
        computer_question = input('Will you be playing a computer or player today?')
        if computer_question == 'computer':
            self.player_one.chosen_gesture = self.human.player_one_turn()
            self.name = 'Computer'
            self.computer.chosen_gesture = self.computer.computer_turn(self.name)
            return [self.player_one.chosen_gesture, self.computer.chosen_gesture]
        elif computer_question == 'player':
            self.player_one.chosen_gesture = self.human.player_one_turn()
            self.player_two.chosen_gesture = self.human.player_two_turn()
            return [self.player_one.chosen_gesture, self.player_two.chosen_gesture]


    def gesture_comparison(self):
        chosen_gestures = self.computer_player()
        if chosen_gestures[0] == 'rock' and chosen_gestures[1] == 'scissors':
            print('Rock Crushes Scissors')
        elif chosen_gestures[0] == 'Scissors' and chosen_gestures[1] == 'paper':
            print('Scissors cuts Paper')
        elif chosen_gestures[0] == 'paper' and chosen_gestures[1] == 'rock':
            print('Paper covers Rock.')