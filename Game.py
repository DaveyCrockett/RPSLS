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
            players = [self.player_one, self.computer]
            while k < 3:
                if players[0].score == 2 or players[1].score == 2:
                    self.diplay_winner(players)
                    break
                else:
                    self.player_one.name = input('Enter player one name here: ')
                    self.computer.name = 'Computer'
                    print(self.player_one.name + ' is first to go.')
                    self.player_one.choice = self.human.human_choice()
                    print(self.computer.name + ' is next.')
                    self.computer.choice = self.computer.computer_choice()
                    print(self.computer.name + ' choice is: ' + self.computer.choice)
                    self.gesture_comparison(players)
                k += 1
            self.diplay_winner(players)
        elif computer_question == 'player':
            k = 1
            players = [self.player_one, self.player_two]
            while k < 4:
                if players[0].score == 2 or players[1].score == 2:
                    self.diplay_winner(players)
                    break
                else:
                    self.player_one.name = input('Enter player one name here: ')
                    self.player_two.name = input('Enter player two name here: ')
                    print(self.player_one.name + ' is first to go.')
                    self.player_one.choice = self.human.human_choice()
                    print(self.player_two.name + ' is next')
                    self.player_two.choice = self.human.human_choice()
                    self.gesture_comparison(players)
                k += 1
            self.diplay_winner(players)

    def gesture_comparison(self, players):
        length = len(players)
        for i in range(length):
            for j in range(i):
                player_compare = self.comparison(players[j], players[i])
                print(players[j].name + ' score is: ' + str(player_compare[0]))
                print(players[i].name + ' score is: ' + str(player_compare[1]))


    def comparison(self, player_one, player_two):
        if 'rock' in (player_one.choice, player_two.choice) and 'scissors' in (player_one.choice, player_two.choice):
            print('Rock Crushes Scissors')
            if player_one.choice == 'rock':
                player_one.score += 1
                player_two.score += 0
                return [player_one.score, player_two.score]
            elif player_two.choice == 'rock':
                player_one.score += 0
                player_two.score += 1
                return [player_one.score, player_two.score]
        elif 'scissors' in (player_one.choice, player_two.choice) and 'paper' in (player_one.choice, player_two.choice):
            print('Scissors cuts Paper')
            if player_one.choice == 'scissors':
                player_one.score += 1
                player_two.score += 0
                return [player_one.score, player_two.score]
            elif player_two.choice == 'scissors':
                player_one.score += 0
                player_two.score += 1
                return [player_one.score, player_two.score]
        elif 'paper' in (player_one.choice, player_two.choice) and 'rock' in (player_one.choice, player_two.choice):
            print('Paper covers Rock.')
            if player_one.choice == 'paper':
                player_one.score += 1
                player_two.score += 0
                return [player_one.score, player_two.score]
            elif player_two.choice == 'paper':
                player_one.score += 0
                player_two.score += 1
                return [player_one.score, player_two.score]
        elif 'rock' in (player_one.choice, player_two.choice) and 'lizard' in (player_one.choice, player_two.choice):
            print('Rock crushes Lizard.')
            if player_one.choice == 'rock':
                player_one.score += 1
                player_two.score += 0
                return [player_one.score, player_two.score]
            elif player_two.choice == 'rock':
                player_one.score += 0
                player_two.score += 1
                return [player_one.score, player_two.score]
        elif 'lizard' in (player_one.choice, player_two.choice) and 'Spock' in (player_one.choice, player_two.choice):
            print('Lizard poisons Spock')
            if player_one.choice == 'lizard':
                player_one.score += 1
                player_two.score += 0
                return [player_one.score, player_two.score]
            elif player_two.choice == 'lizard':
                player_one.score += 0
                player_two.score += 1
                return [player_one.score, player_two.score]
        elif 'Spock' in (player_one.choice, player_two.choice) and 'scissors' in (player_one.choice, player_two.choice):
            print('Spock smashes scissors.')
            if player_one.choice == 'Spock':
                player_one.score += 1
                player_two.score += 0
                return [player_one.score, player_two.score]
            elif player_two.choice == 'Spock':
                player_one.score += 0
                player_two.score += 1
                return [player_one.score, player_two.score]
        elif 'scissors' in (player_one.choice, player_two.choice) and 'lizard' in (player_one.choice, player_two.choice):
            print('Scissors decapitates lizard')
            if player_one.choice == 'scissors':
                player_one.score += 1
                player_two.score += 0
                return [player_one.score, player_two.score]
            elif player_two.choice == 'scissors':
                player_one.score += 0
                player_two.score += 1
                return [player_one.score, player_two.score]
        elif 'lizard' in (player_one.choice, player_two.choice) and 'paper' in (player_one.choice, player_two.choice):
            print('Lizard eats Paper')
            if player_one.choice == 'lizard':
                player_one.score += 1
                player_two.score += 0
                return [player_one.score, player_two.score]
            elif player_two.choice == 'lizard':
                player_one.score += 0
                player_two.score += 1
                return [player_one.score, player_two.score]
        elif 'paper' in (player_one.choice, player_two.choice) and 'Spock' in (player_one.choice, player_two.choice):
            print('Paper disproves Spock')
            if player_one.choice == 'paper':
                player_one.score += 1
                player_two.score += 0
                return [player_one.score, player_two.score]
            elif player_two.choice == 'paper':
                player_one.score += 0
                player_two.score += 1
                return [player_one.score, player_two.score]
        elif 'Spock' in (player_one.choice, player_two.choice) and 'rock' in (player_one.choice, player_two.choice):
            print('Spock Vaporizes Rock')
            if player_one.choice == 'Spock':
                player_one.score += 1
                player_two.score += 0
                return [player_one.score, player_two.score]
            elif player_two.choice == 'Spock':
                player_one.score += 0
                player_two.score += 1
                return [player_one.score, player_two.score]
        elif player_one.choice == player_two.choice:
            print('We have a tie!')
            player_one.score += 0
            player_two.score += 0
            return[player_one.score, player_two.score]

    def diplay_winner(self, players):
        if players[0].score > players[1].score:
            print(players[0].name + ' is the winner!')
        elif players[1].score > players[0].score:
            print(players[1].name + ' is the winner!')
        elif players[1].score == players[0].score:
            print('We have a tie for the whole game!')