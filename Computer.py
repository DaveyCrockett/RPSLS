from Player import Player

import random


class Computer(Player):
    def __init__(self):
        super().__init__()

    def computer_choice(self):
       choice = random.choice(self.chosen_gesture)
       return choice
