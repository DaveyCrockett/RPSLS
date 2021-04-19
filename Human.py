from Player import Player


class Human(Player):
    def __init__(self):
        super().__init__()

    def player_choice(self):
        print('The choices are: ' + str(self.chosen_gesture))
        while True:
            player_gesture = input('Enter your choice of gesture.')
            if any(item.lower() == player_gesture.lower() for item in self.chosen_gesture):
                print('Thats a great choice')
                break
            print('Not one of the choices.')


