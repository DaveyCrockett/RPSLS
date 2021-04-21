from Player import Player

import random


class Computer(Player):
    def __init__(self):
        super().__init__()

    def computer_choice(self):
        rando = random.choice(self.chosen_gesture) # rando may be the problem
        print(self.name + ' chooses ' + rando)
        return rando

    def computer_turn(self):
        computer_round = self.computer_choice()
        return computer_round
