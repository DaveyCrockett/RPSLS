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
        self.computer_player()

    def welcome(self):
        print('Welcome to RPSLS or better known as Rock, Paper, Scissors, Lizard, Spock.')

    def computer_player(self):
        computer_question = input('Will you be playing a computer or player today?')
        if computer_question == 'computer':
            k = 1
            while k < 3:
                self.player_one.name = input('Enter player one name here: ')
                self.computer.name = 'Computer'
                print(self.player_one.name + ' is first to go.')
                self.player_one.chosen_gesture = self.human.human_choice()
                print(self.computer.name + ' is next.')
                self.computer.chosen_gesture = self.computer.computer_turn()
                players = [self.player_one, self.computer]
                self.gesture_comparison(players)
                k += 1
        elif computer_question == 'player':
            k = 1
            while k < 3:
                self.player_one.name = input('Enter player one name here: ')
                self.player_two.name = input('Enter player two name here: ')
                print(self.player_one.name + ' is first to go.')
                self.player_one.chosen_gesture = self.human.human_choice()
                print(self.player_two.name + ' is next')
                self.player_two.chosen_gesture = self.human.human_choice()
                players = [self.player_one, self.player_two]
                self.gesture_comparison(players)
                k += 1

    # TODO Add scoring to gesture_comparison

    def gesture_comparison(self, players):
        length = len(players)
        for i in range(length):
            for j in range(i):
                player_compare = self.comparison(players[i], players[j])
                print(players[i].name + ' score is: ' + str(player_compare[0]))
                print(players[j].name + ' score is: ' + str(player_compare[1]))


    def comparison(self, player_one, player_two):
        if 'rock' in (player_one.chosen_gesture, player_two.chosen_gesture) and 'scissors' in (player_one.chosen_gesture, player_two.chosen_gesture):
            print('Rock Crushes Scissors')
            if player_one.chosen_gesture == 'rock':
                self.player_one.score += 1
                self.player_two.score += 0
                return [self.player_one.score, self.player_two.score]
            elif player_two.chosen_gesture == 'rock':
                self.player_one.score += 0
                self.player_two.score += 1
                return [self.player_one.score, self.player_two.score]
        elif 'scissors' in (player_one.chosen_gesture, player_two.chosen_gesture) and 'paper' in (player_one.chosen_gesture, player_two.chosen_gesture):
            print('Scissors cuts Paper')
            if player_one.chosen_gesture == 'scissors':
                self.player_one.score += 1
                self.player_two.score += 0
                return [self.player_one.score, self.player_two.score]
            elif player_two.chosen_gesture == 'scissors':
                self.player_one += 0
                self.player_two.score += 1
                return [self.player_one.score, self.player_two.score]
        elif 'paper' in (player_one.chosen_gesture, player_two.chosen_gesture) and 'rock' in (player_one.chosen_gesture, player_two.chosen_gesture):
            print('Paper covers Rock.')
            if player_one.chosen_gesture == 'paper':
                self.player_one.score += 1
                self.player_two.score += 0
                return [self.player_one.score, self.player_two.score]
            elif player_two.chosen_gesture == 'paper':
                self.player_one.score += 0
                self.player_two.score += 1
                return [self.player_one.score, self.player_two.score]
        elif 'rock' in (player_one.chosen_gesture, player_two.chosen_gesture) and 'lizard' in (player_one.chosen_gesture, player_two.chosen_gesture):
            print('Rock crushes Lizard.')
            if player_one.chosen_gesture == 'rock':
                self.player_one.score += 1
                self.player_two.score += 0
                return [self.player_one.score, self.player_two.score]
            elif player_two.chosen_gesture == 'rock':
                self.player_one += 0
                self.player_two.score += 1
                return [self.player_one.score, self.player_two.score]
        elif 'lizard' in (player_one.chosen_gesture, player_two.chosen_gesture) and 'Spock' in (player_one.chosen_gesture, player_two.chosen_gesture):
            print('Lizard poisons Spock')
            if player_one.chosen_gesture == 'lizard':
                self.player_one.score += 1
                self.player_two.score += 0
                return [self.player_one.score, self.player_two.score]
            elif player_two.chosen_gesture == 'lizard':
                self.player_one += 0
                self.player_two.score += 1
                return [self.player_one.score, self.player_two.score]
        elif 'Spock' in (player_one.chosen_gesture, player_two.chosen_gesture) and 'scissors' in (player_one.chosen_gesture, player_two.chosen_gesture):
            print('Spock smashes scissors.')
            if player_one.chosen_gesture == 'Spock':
                self.player_one.score += 1
                self.player_two.score += 0
                return [self.player_one.score, self.player_two.score]
            elif player_two.chosen_gesture == 'Spock':
                self.player_one += 0
                self.player_two.score += 1
                return [self.player_one.score, self.player_two.score]
        elif 'scissors' in (player_one.chosen_gesture, player_two.chosen_gesture) and 'lizard' in (player_one.chosen_gesture, player_two.chosen_gesture):
            print('Scissors decapitates lizard')
            if player_one.chosen_gesture == 'scissors':
                self.player_one.score += 1
                self.player_two.score += 0
                return [self.player_one.score, self.player_two.score]
            elif player_two.chosen_gesture == 'scissors':
                self.player_one += 0
                self.player_two.score += 1
                return [self.player_one.score, self.player_two.score]
        elif 'lizard' in (player_one.chosen_gesture, player_two.chosen_gesture) and 'paper' in (player_one.chosen_gesture, player_two.chosen_gesture):
            print('Lizard eats Paper')
            if player_one.chosen_gesture == 'lizard':
                self.player_one.score += 1
                self.player_two.score += 0
                return [self.player_one.score, self.player_two.score]
            elif player_two.chosen_gesture == 'lizard':
                self.player_one.score += 0
                self.player_two.score += 1
                return [self.player_one.score, self.player_two.score]
        elif 'paper' in (player_one.chosen_gesture, player_two.chosen_gesture) and 'Spock' in (player_one.chosen_gesture, player_two.chosen_gesture):
            print('Paper disproves Spock')
            if player_one.chosen_gesture == 'paper':
                self.player_one.score += 1
                self.player_two.score += 0
                return [self.player_one.score, self.player_two.score]
            elif player_two.chosen_gesture == 'paper':
                self.player_two.score += 1
                return [self.player_one.score, self.player_two.score]
        elif 'Spock' in (player_one.chosen_gesture, player_two.chosen_gesture) and 'rock' in (player_one.chosen_gesture, player_two.chosen_gesture):
            print('Spock Vaporizes Rock')
            if player_one.chosen_gesture == 'Spock':
                self.player_one.score += 1
                self.player_two.score += 0
                return [self.player_one.score, self.player_two.score]
            elif player_two.chosen_gesture == 'Spock':
                self.player_one.score += 0
                self.player_two.score += 1
                return [self.player_one.score, self.player_two.score]
        else:
           print('We have a tie!')
