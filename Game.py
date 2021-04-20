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

    # TODO Add scoring to gesture_comparison

    def gesture_comparison(self):
        chosen_gestures = self.computer_player()
        length = len(chosen_gestures)
        for i in range(length):
            for j in range(i +1, length):
                self.comparison(chosen_gestures[i], chosen_gestures[j])

    def comparison(self, player_one, player_two):
        if player_one or player_two == 'rock' and player_two or player_one == 'scissors':
            print('Rock Crushes Scissors')
        elif player_one or player_two == 'Scissors' and player_one or player_two == 'paper':
            print('Scissors cuts Paper')
        elif player_one or player_two == 'paper' and player_one or player_two == 'rock':
            print('Paper covers Rock.')
        elif player_one or player_two == 'rock' and player_one or player_two == 'lizard':
            print('Rock crushes Lizard.')
        elif player_one or player_two == 'lizard' and player_one or player_two == 'Spock':
            print('Lizard poisons Spock')
        elif player_one or player_two == 'Spock' and player_one or player_two == 'Scissors':
            print('Spock smashes scissors.')
        elif player_one or player_two == 'Scissors' and player_one or player_two == 'lizard':
            print('Scissors decapitates lizard')
        elif player_one or player_two == 'Scissors' and player_one or player_two == 'lizard':
            print('Scissors decapitates lizard')
