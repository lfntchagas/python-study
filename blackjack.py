import random 

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}


playing = True

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'



class Deck:
    
    def __init__(self):
        self.deck = []

        for suit in suits:
            for rank in ranks:
                new_card = Card(suit, rank) # instantiate each card in the for loop with the class Card, then append it to the list self.deck
                self.deck.append(new_card)

    def __str__(self):
        return f'deck class' 


    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)

    def adjust_for_ace(self):
        pass


class Chips:

    def __init__(self):
        self.total = 100 

    def win_bet(self, value_bet):
        self.total += value_bet

    def lose_bet(self, value_bet):
        self.total -= value_bet


def take_bet(user_chip):

    while True:

        try:
            bet = int(input('Type the value for the bet\n'))
            if bet < user_chip.total:
                return bet

        except:

            print("An error occured! \n")
            continue

        else:
            print('You dont have money enough')


def hit(deck, hand):

    pop_card = deck.deal()
    
    if hand.value > 21:
        print('You bust!!')

    elif pop_card.rank == 'Ace':

        if hand.value + pop_card.value > 21:
            hand.value += 1
            print('Aces value is 1')
            hand.add_card(pop_card)

        else:
            hand.value += pop_card.value
            print(f'Aces value is {pop_card.value}')
            hand.add_card(pop_card)

    else:
        
        print('card is: ', pop_card)
        hand.value += pop_card.value
        hand.add_card(pop_card)




def hit_or_stand(deck, hand):
    global playing

    user_choice = input('Type Hit or Stand\n').lower()

    if user_choice == 'hit':
        hit(deck, hand)

    else:
        print('player has choose to stand')
        playing = False
    

def show_some(player, dealer):
    print('\nDealer cards are:')
    for card in dealer.cards[1:]:
        print(card)
    

    print('\nPlayer cards are:')
    for card in player.cards:
        print(card)
  

def show_all(player,dealer):

    print('\nDealer cards are:')
    for card in dealer.cards:
        print(card)
    print(f'Dealer hands value is {player.value}')

    print('\nPlayer cards are:')
    for card in player.cards:
        print(card)

    print(f'Player hands value is {dealer.value}')


def player_busts(player_hand, player_chips):

    print(f'Player hand is over 21. current player hand is {player_hand.value}')
    player_chips.lose_bet(take_bet(player_chips))
    print(f'Player has now {player_chips.total} Chips :(')
        

def player_wins(player_hand, player_chips):
    print(f'Player WINS! current player hand is {player_hand.value}')
    player_chips.win_bet(take_bet(player_chips))
    print(f'Player has now {player_chips.total} Chips!!')
        

def dealer_busts(dealer_hand, player_chips):
    print(f'Dealer LOST! Dealers hand is {dealer_hand.value}')
    bet_value = take_bet(player_chips) * 2
    player_chips.win_bet(bet_value)
    print(f'Player has now {player_chips.total} Chips!!')
    


    
def dealer_wins():
    pass
    
def push():
    pass


red_deck = Deck() # Initialize the deck
player1_chips = Chips()
player1 = Hand()


#player_wins(player1, player1_chips)
dealer_busts(player1, player1_chips)




dealer = Hand()

hit(red_deck, player1)
hit(red_deck, dealer)

show_all(player1,dealer)



# while playing:
    
#     hit_or_stand(red_deck, player1)



                





# Rules:

# 1 - Player keeps hitting goes over 21, they bust and lost the bet. The game is then over and dealer collects the money. That happens even before the dealer start.

# 2 - The computer Dealer beats the Player. Computer sum higher than player sum and still under 21.  If Player is under 21, dealer then hits until they either beat the player or the dealer bust.

# 3 - Player wins after computer dealer goes over 21. If player is under 21, dealer then hits until they either beat the player or the dealer busts . receives double bet