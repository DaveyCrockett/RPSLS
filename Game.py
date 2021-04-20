from Player import Player
from Computer import Computer

class Game:
    def __init__(self):
        self.player_one = Player()
        self.player_two = Player()
        self.computer = Computer()

    def run_game(self):
        self.computer.computer_player()



