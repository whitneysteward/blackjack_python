import random

print ("Hello! You're playing blackjack!")
class Card:
    def __init__(self, suit, face, value):
        self.suit = suit
        self.face = face
        self.value = value

    def __str__(self):
        return '{f} of {s}'.format(f=self.face, s=self.suit)

    def __repr__(self):
        return '{f} of {s}'.format(f=self.face, s=self.suit)


class Deck:
    def __init__(self):
        self.deck = self.create_deck()
        self.shuffle_deck()

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def create_deck(self):
        deck = []
        suit = ['Diamonds', 'Hearts', 'Clubs', 'Spades']
        face = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9',
                '10', 'Jack', 'Queen', 'King']
        value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        for s in suit:
            x = 0
            for f in face:
                card = Card(s, f, value[x])
                deck.append(card)
                x += 1


        return deck

class Hand:
    def __init__(self, name):
        self.name = name
        self.cards = []
        #self.sum = sum
    def draw(player,deck):
        player.cards.append(deck.deck.pop())
        player.cards.append(deck.deck.pop())
    #append adds to the end and then pop deletes from deck

    #put hand create a list of players
deck = Deck()
user = int(input ("How many players are there?"))
players = []
for re in range(1, user + 1):
    player = Hand(input("Player {}, What is your name? ".format(re)))
    players.append(player)

for name in players:
    draw(name,deck)
    print(name.cards)
