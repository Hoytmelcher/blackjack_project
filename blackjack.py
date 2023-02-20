import random

suits = ("Spades", "Hearts", "Clubs", "Diamonds")
names = (
    'Two', 'Three', 'Four', 'Five', 
    'Six', 'Seven', 'Eight', 'Nine', 'Ten',
    'Jack', 'Queen', 'King', 'Ace',
)
 
values = {
    'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 
    'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 
    'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11,
}

    
class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for name in names:
                self.deck.append((suit, name))

    def shuffle(self):
        random.shuffle(self.deck)

    def hit_me(self):
        deal_card = self.deck.pop()
        return deal_card
    
    def deal(self):
        deal_card = self.deck.pop()
        return deal_card

class Hand:
    def __init__(self):
        self.hand = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.hand.append(card)
        self.value += values[card[1]]

    def ace_adjust(self):
        if self.hand[0][1] == "Ace" or self.hand[1][1] == "Ace":
            if self.value <11:
                values["Ace"] = 11
            else:
                values["Ace"] = 1


class Chip:
    def __init__(self):
        self.total = 200
        self.bet = 0
    
    def win(self):
        self.total = self.total + self.bet

    def lose(self):
        self.total = self.total - self.bet

    def draw(self):
        self.total = self.total


def place_bet(chips):
    chips.bet = int(input("Place your bets! "))
    if chips.total == 0 and chips.bet > chips.total:
        raise Exception("you're out of chips, better luck next time!")
    while chips.bet > chips.total or not (isinstance(chips.bet, int)):
        chips.bet = int(input("Place your bets! "))

def hit(deck, hand):
    hand.add_card(deck.hit_me())
    hand.ace_adjust()

def hit_or_stay(deck, hand):
    while True:
        hos = input("Will you hit or Stay?(h/s): ").lower()
        if hos == "h":
            print("Player hits")
            hit(deck, hand) 
        else:
            print("Player stannds, dealer plays.")
            return False
        return True
    
def game_hands(dealer_hand, player_hand):
    print(f'DEALER: {dealer_hand.hand[0]}')
    print(f'PLAYER: {str(player_hand.hand)} {str(player_hand.value)}')

def end_hands(dealer_hand, player_hand):
    print(f'DEALER: {dealer_hand.hand} {dealer_hand.value}')
    print(f'PLAYER: {player_hand.hand} {player_hand.value}')
    
def player_bust(chips):
    chips.lose()
    print("Player busts!")

def player_win(chips):
    chips.win()
    print("Player wins!")

def dealer_bust(chips):
    chips.win()
    print("Dealer busts!")

def dealer_win(chips):
    chips.lose()
    print("Dealer Wins!")

def draw(chips):
    print("Draw!")
    chips.draw()

def play_again():
    again = input("Would you like to keep playing?(y/n): ").lower()
    if again == "y":
        return True

def game():
    win = 0
    loss = 0
    draws = 0
    chips = Chip()
    print(f'Current chips: {chips.total}')
    while True:
        deck = Deck()
        deck.shuffle()
        dealer_hand = Hand()
        player_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())
        if chips.total == 0:
            print("you're out of chips, better luck next time!")
            return False
        place_bet(chips)
        game_hands(dealer_hand, player_hand)
        if player_hand.value == 21:
            print("Winner winner, chicken dinner!")
            player_win(chips)
            win += 1
            continue
        while hit_or_stay(deck, player_hand):
            game_hands(dealer_hand, player_hand)
            if player_hand.value > 21:
                end_hands(dealer_hand, player_hand)
                player_bust(chips)
                loss += 1
                print(f"Wins  =  {win},Loses =  {loss}, Draw  =  {draws}")
                break
        if player_hand.value <= 21:
            while dealer_hand.value < 17:
                hit(deck, dealer_hand)
            end_hands(dealer_hand, player_hand)
            if dealer_hand.value > 21:
                dealer_bust(chips)
                win += 1
                print(f"Wins  =  {win},Loses =  {loss}, Draw  =  {draws}")
            elif dealer_hand.value > player_hand.value:
                dealer_win(chips)
                loss += 1
                print(f"Wins  =  {win},Loses =  {loss}, Draw  =  {draws}")
            elif dealer_hand.value < player_hand.value:
                player_win(chips)
                win += 1
                print(f"Wins  =  {win},Loses =  {loss}, Draw  =  {draws}")
            else:
                draw(chips)
                draws += 1
                print(f"Wins  =  {win},Loses =  {loss}, Draw  =  {draws}")
        print(f'Total chips: {chips.total}')
        if play_again():
            continue
        else:
            print("Thank you for playing, come again!")
            print(f"Total Wins  =  {win}, Total Loses =  {loss}, Total Draws  =  {draws}")
            break

game()

            
