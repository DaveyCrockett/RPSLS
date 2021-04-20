from Player import Player
from Human import Human
import random
class Computer(Player):
    def __init__(self):
        super().__init__()

    def computer_choice(self):
        self.name = 'Computer'
        rando = random.choice(self.chosen_gesture)
        print(self.name + ' chooses ' + rando)
        return rando

    def computer_player(self):
        computer_question = input('Will you be playing a computer or player today?')
        if computer_question == 'computer':
            self.name = 'Computer'
            self.play_game(self.name)
        elif computer_question == 'player':
            Human().play_game()


    def computer_turn(self, computer):
        print(computer + ' is next.')
        computer_turn = self.computer_choice()
