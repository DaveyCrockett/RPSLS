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

    def computer_turn(self, computer):
        print(computer + ' is next.')
        computer_round = self.computer_choice()
        return computer_round
