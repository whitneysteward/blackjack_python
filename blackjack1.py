''' Blackjack
            rules: dealer freezes at 17, player plays until they reach 21 or bust (more than)

list of player
    get name

Deck
    cards
dealer

Deck
    cards


    face cards
    value for cards
sum of cards
shuffle



'''
import random

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.thing = {
            1:'Ace',
            2:'Two',
            3:'Three',
            4:'Four',
            5:'Five',
            6:'Six',
            7:'Seven',
            8:'Eight',
            9:'Nine',
            10:'Ten',
            11:'Jack',
            12:'Queen',
            13:'King'}
        self.thing2 ={1:'Hearts', 2:'Spades', 3:'Clubs', 4:'Diamonds'}
        self.thing3 = {'King' : 10, 'Queen' : 10, 'Jack' : 10}
#this is returning the dealer's list of cards
    def __repr__(self):
        return '{} of {}'.format(self.thing[self.value], self.thing2[self.suit])

class Deck:
    def __init__(self):
        self.cards = []
        #self.cards = list()

    def shuffle (self):
        random.shuffle(self.cards)

        for i in range(len(self.cards)):
            card = self.cards[i]

            print(' {} of {}'.format(card.thing[card.value],card.thing2[card.suit]))




    def sum (self):
        print ('Sum for players, inside their deck')

    def addcards(self):
        value = random.randint(1, 13)
        suit = random.randint( 1, 4)
        card = Card(value, suit)
        self.cards.append(card)
        #added card
        print(' {} of {}'.format(card.thing[value],card.thing2[suit]))


class Hand:
    def __init__(self, name):
        value = random.randint(1, 13)
        suit = random.randint( 1, 4)
        card = Card(value, suit)
        self.cards = []
        self.cards.append(card)
        self.name = name
        self.total = 0
        #added card
        print(' {} of {}'.format(card.thing[value],card.thing2[suit]))
        value2 = random.randint(1, 13)
        suit2 = random.randint( 1, 4)
        card2 = Card(value2, suit2)

        self.cards.append(card2)
        #added card
        if self.name != "Dealer":
            print(' {} of {}'.format(card2.thing[value2],card2.thing2[suit2]))

        # card2_value = card2.thing3[card2.suit]
        # look up value of the number of the card in the thing3 dictionary
        # assign the value to card2_value
        # do the same thing for card1
        # add those two together to get the correct self.sum


        if self.name != 'Dealer':
            self.sum()
            print ('Here is the sum of your two cards!= {}'.format(self.total))

    def sum (self):
        self.total = 0
        Ace = 0
        for card in self.cards:
            if card.value == 1:
                Ace += 1
                if Ace > 1:
                    self.total += 1
            elif card.value == 11 or card.value == 12 or card.value == 13:
                print('10')
                self.total += 10
            else:
                self.total += card.value
            if Ace > 0 and self.total + 11 < 22:
                    self.total += 11
            elif Ace > 0 and self.total + 11 > 21:
                self.total += 1


    def Hit (self):
        value = random.randint(1, 13)
        suit = random.randint( 1, 4)
        card = Card(value, suit)
        self.cards.append(card)
        print(' Hit added!{} of {}'.format(card.thing[value],card.thing2[suit]))

    def Freeze (self):
        pass
        print('Frozen')

    # def dealer1 (self):
    #         value = random.randint(1, 13)
    #         suit = random.randint( 1, 4)
    #         card = Card(value, suit)
    #         self.cards = []
    #         self.cards.append(card)
    #         print(' {} of {}'.format(card2.thing[value2],card2.thing2[suit2]))

        #gives sum of two cards

#deck = Deck()
#deck.addcards()
#deck.addcards()

#print("Starting to Shuffle!")
#deck.shuffle()
print ('Player\'s deck')
player_hand = Hand('Player')
print ('Dealer\'s deck')
dealer_hand = Hand('Dealer')


player_turn = True
while player_turn:
    player_hand.sum()#this is giving hand value for player
    print(player_hand.total)

    user_input = input("Would you like to hit?(y/n)")
    if user_input == 'y':

        player_hand.Hit()

    elif user_input == 'n':
        player_turn = False
    else:
         print('I don\'t understand! Please pick y or n!')


print('Dealers turn')
dealer_hand.sum()
if dealer_hand.total< 17:
    dealer_hand.Hit()
if dealer_hand.total >= 17:
    dealer_hand.Freeze()

player_hand.sum()
if player_hand.total == 21:
     print('You/ve won!')
     print(dealer_hand.cards)
if player_hand.total >21:
     print('BUSTED')
     print(dealer_hand.cards)
