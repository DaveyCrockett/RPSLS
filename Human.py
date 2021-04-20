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

    def player_one_turn(self):
        self.name = input('Enter player one name here: ')
        print(self.name + ' is first to go.')
        player_one_round = self.human_choice()
        return player_one_round

    def player_two_turn(self):
        self.name = input('Enter player two name here: ')
        player_two_round = self.human_choice()
        return player_two_round




