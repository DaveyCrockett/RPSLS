from Player import Player


class Human(Player):
    def __init__(self):
        super().__init__()

    def human_choice(self):
        print('The choices are: ' + str(self.chosen_gesture))
        while True:
            player_gesture = input('Enter your choice of gesture.')
            if any(item.lower() == player_gesture.lower() for item in self.chosen_gesture):
                print('Thats a great choice')
                return player_gesture
            print('Not one of the choices.')

    def play_game(self):
        self.name = input('Enter your name here: ')
        print(self.name + ' is first to go.')
        player_one_turn = self.human_choice()
        self.name = input('Enter your name here: ')
        print(self.name + ' is next.')
        player_two_turn = self.human_choice()
        if player_one_turn == 'rock' and player_two_turn == 'scissors':
            print('Rock Crushes Scissors')
        elif player_one_turn == 'Scissors' and player_two_turn == 'paper':
            print('Scissors cuts Paper')
        elif player_one_turn == 'paper' and player_two_turn == 'rock':
            print('Paper covers Rock.')

