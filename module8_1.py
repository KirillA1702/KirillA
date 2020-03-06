import random
import sys
import time

class Loto:

    def __init__(self, amount_card):
        row = 3
        self.all_row = row * amount_card
        self.set_card()

    def set_card(self):
        num = set()
        while len(num) < self.all_row * 5:
            num.add(random.randint(1, 99))
        cards = list(num)
        random.shuffle(cards)

        while len(cards) % self.all_row != 0:
            cards.append('')
        self.all_row = int(len(cards) / self.all_row)
        cards = [cards[i: i + self.all_row] for i in range(0, len(cards), self.all_row)]

        for i in range(len(cards)):
            cards[i].sort()
        self.card_user = cards[:3]
        self.card_comp = cards[3:]

    def get_card(self, card_player):
        print('{:-^25}'.format(self.name))
        print('{0[0]:>2} {0[1]:<10} {0[2]:<5} {0[3]} {0[4]} '.format(card_player[0]))
        print('{0[0]:>3} {0[1]:<6} {0[2]:<7} {0[3]:<3} {0[4]} '.format(card_player[1]))
        print('{0[0]:<3} {0[1]:<7} {0[2]:<2} {0[3]:<5} {0[4]} '.format(card_player[2]))
        print('{:-^25}'.format('-'))

    def search(self, card_player, num_cask):
        for i, n in enumerate(card_player):
            if num_cask in n:
                card_player[i][n.index(num_cask)] = '-'
                self.score += 1
                if self.score == 15:
                    print('{} Победила!'.format(self.name))
                    sys.exit(1)
                return True
        return False

class Keg:

    def __init__(self, amount):
        self.amount = amount
        self.gen = self.find()

    def find(self):
        arr = [x for x in range(1, self.amount + 1)]
        random.shuffle(arr)
        for i, y in enumerate(arr):
            print(f'{" " * 30}')
            print(f'Новый бочонок: {y} (осталось {self.amount - (i + 1)})')
            yield y

class Player(Loto):

    def __init__(self, name):
        self.name = name
        self.score = 0

def game_start():
    game = Loto(2)
    keg = Keg(99)
    player1 = Player('Ваша карточка')
    player2 = Player('Карточка компьютера')

    while True:
        num_keg = next(keg.gen)
        player1.get_card(game.card_user)
        player2.get_card(game.card_comp)

        user_inp = input('Зачеркнуть цифру? (y/n)\n')
        if user_inp == 'y':
            if player1.search(game.card_user, num_keg):
                continue
            else:
                print('Game Over')
                sys.exit(1)
        if user_inp == 'n':
            if player1.search(game.card_user, num_keg):
                print('Game Over')
                sys.exit(1)
            elif player2.search(game.card_comp, num_keg):
                continue
        if user_inp != 'n' and user_inp != 'y':
            print('Введите y or n')
            time.sleep(1)
            continue

game_start()