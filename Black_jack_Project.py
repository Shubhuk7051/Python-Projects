import random

suits=('Hearts','Diamonds','Spades','Clubs')
ranks=('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values={'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
        'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


playing=True

#Classes

class Card: #Creates all the cards

    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank

    def __str__(self):
        return self.rank + ' of ' +self.suit #Ex- King of Hearts

class Deck: #Create a Deck of Cards

    def __init__(self):
        self.deck=[] #Haven't created a deck yet

        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_comp='' #Haven't created a combinaton of cards
        for card in self.deck:
            card_name=card.__str__()
            deck_comp+='\n' + card_name
        return 'The deck has: ' + deck_comp

    def shuffle(self): #shuffle all the card in the deck
        random.shuffle(self.deck)

    def deal(self): #Pick out a card from the deck
        single_card=self.deck.pop() #Pop out last card of self.deck list
        return single_card

class Hand: #Show all the cards that the player or dealer have

    def __init__(self):
        self.cards=[]
        self.value=0
        self.aces=0 #Keep track of aces

    def add_card(self,card): #Add a card to the player's or dealer's hand
        self.cards.append(card)
        self.value+=values[card.rank]
        if card.rank == 'Ace':
            self.aces+=1

    def adjust_for_ace(self): #Adjust ace if value is greater than 21 then value of ace is 1 otherwise 11
        while self.value > 21 and self.aces:
            self.value-=10
            self.aces-=1

class Chips: #Keep track of chips

    def __init__(self):
        self.total=100
        self.bet=0

    def win_bet(self):
        self.total+=self.bet

    def lose_bet(self):
        self.total-=self.bet

#FUNCTIONS

def take_bet(chips): #Ask for user/player bet

    while True:
        try:
            chips.bet=int(input("How many chips would you like to bet?"))
        except ValueError:
            print("Sorry! Please can youn type in a number:")
        else:
            if chips.bet > chips.total:
                print("Your bet can't exceed 100!")
            else:
                break

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck,hand): #hit or stand
    global playing
    while True:
        ask=input("\nWould you like to hit or stand? Please enter 'h' or 's':")

        if ask[0].lower() == 'h':
            hit(deck,hand)
        elif ask[0].lower() == 's':
            print("\nPlayer stands, Dealer is playing.")
            playing=False
        else:
            print("\nSorry! I did not understand that! Please try again!")
            continue
        break

def show_card(player,dealer): #Show card of player's and dealer's hand(During Game)
    print("\nDealer's hand: ")
    print(" <card hidden> ")
    print("", dealer.cards[1])
    print("\nPlayer's hand: ", *player.cards, sep='\n')


def show_all(player,dealer): #Show all card of player's and dealer's hand(End Game)
    print("\nDealer's hand: ", *dealer.cards, sep='\n')
    print("Dealer's hand=", dealer.value)
    print("\nPlayer's hand: ", *player.cards, sep='\n')
    print("Player's hand=", player.value)

#Game Endings

def player_busts(player,dealer,chips): #When player lose
    print("\nPLAYER BUSTS!")
    chips.lose_bet()

def player_wins(player,dealer,chips): #When player win
    print("\nPLAYER WINS!")
    chips.win_bet()

def dealer_busts(player,dealer,chips): #When dealer lose
    print("\nDEALER BUSTS!")
    chips.win_bet()

def dealer_wins(player,dealer,chips): #When dealer win
    print("\nDEALER WINS!")
    chips.lose_bet()

def tie(player,dealer): #When game ties
    print("\nIts a push! Player and Dealer tie!")

#GamePlay!

while True:
    print("Welcome to BlackJack!")


    deck=Deck() #create a shuffle deck
    deck.shuffle()

    player_hand=Hand()
    #Add card on player hand and create a deal also
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand=Hand()
    #Add card on dealer hand and create a deal also
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    #set up the player's chips
    player_chips=Chips()

    #ask player for bet
    take_bet(player_chips)

    #show cards
    show_card(player_hand,dealer_hand)

    while playing:

        hit_or_stand(deck,player_hand) #When player hit or stand
        show_card(player_hand,dealer_hand)


        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
            
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)

    print("\nPlayer's Winnings stand at",player_chips.total)

    new_game=input("\nWould you like play again? Enter 'y' or 'n':")

    if new_game[0].lower()=='y':
        playing==True
        continue
    else:
        print("\nThanks for playing!")
        break

            
        


    

    


    


    
    






 
            

    

    
        
            
