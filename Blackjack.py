#Creating the deck and assigning a value for each type of card
import random
suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}
playing = True

#Making a class which assigns a value/rank to each individual card

class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank + " of " + self.suit
    
#Making a class which creates a deck that holds all 52 cards and can be shuffled
    
class Deck:

    def __init__(self):

        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
        
    def shuffle(self):

        random.shuffle(self.deck)

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n'+ card.__str__()
        return "The deck has: " +deck_comp
    
    def deal(self):
        single_card = self.deck.pop()
        return single_card
    
#Making a 'hand' class that contains the cards held by the player
        
class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
    
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

#Makind a 'chips' class that represends the player's balance
            
class Chips:
    
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

#Classes and here

#Making a function that takes player's bet
        
def take_bet(chips):
    
    while True:

        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except:
            print("Sorry please pro1vide an integer greater than 0")
        else:
            if chips.bet > chips.total:
                print("Sorry, you do not have enough chips! You have: {} chips available to bet. ".format(chips.total))
            elif chips.bet == 0:
                print("You must bet at least 1")
            else:
                break

#Making a function for when the player chooses "HIT"
            
def hit(deck,hand):

    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

#Making a function to prompt the player to either "HIT" or "STAND"
    
def hit_or_stand(deck,hand):
    
    global playing

    while True:

        x = input('Hit or Stand? Enter h or s ')

        if x[0].lower() == 'h':
            hit(deck,hand)
        
        elif x[0].lower() == 's':
            print("Player stands, Dealer's turn")
            playing = False
        
        else:
            print("Sorry, I did not understand that, Please enter h or s only!")
            continue

        break

#Making two functions to display cards depending on the position of the game
    
def show_some(player,dealer):

    print("\n Dealer's hand: ")
    print("First carrd hidden!")
    print(dealer.cards[1])

    print("\n Player's hand:")
    for card in player.cards:

        print(card)
    print(f"Value of Player's hand is:{player.value}")
    
def show_all(player,dealer):
    
    print("\n Player's hand:")
    for card in player.cards:
        print(card)
    print(f"Value of Player's hand is:{player.value}")

    print("\n Dealer's hand:")
    for card in dealer.cards:
        print(card)
    print(f"Value of Dealer's hand is:{dealer.value}")

#Making functions for each individual end game scenario
    
def player_busts(player,dealer,chips):
    print("Player busts :(")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player WINS :D")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busted, Player wins! :D")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("Dealer wins! :(")
    chips.lose_bet()

def push(player,dealer):
    print('Dealer and player tie! PUSH!')

#Game logic starts  here
    
player_chips = Chips()
    
while True:
   
    print("Hello, welcome to Blackjack!")
     
    #Creating a deck, shuffling it, and dealing two cards to each the player, and the dealer

    play_deck = Deck()
    play_deck.shuffle()
    player_hand = Hand()
    player_hand.add_card(play_deck.deal())
    player_hand.add_card(play_deck.deal())
    dealer_hand = Hand()
    dealer_hand.add_card(play_deck.deal())
    dealer_hand.add_card(play_deck.deal())

    #Taking the bet from the player

    take_bet(player_chips)
    show_some(player_hand,dealer_hand)

    while playing:

        hit_or_stand(play_deck,player_hand)
        show_some(player_hand,dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)

            break
    
    if player_hand.value <= 21:

        while dealer_hand.value < player_hand.value:
            hit(play_deck,dealer_hand)

        show_all(player_hand,dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)
    
    print("\n Player total chips are at: {}".format(player_chips.total))

    if player_chips.total == 0:
        print ("Sorry, unfortunately you are out of funds.")
        break

    new_game = input('Would you like to play another hand? y/n')
   
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thanks for playing!")
        break

#Game ends