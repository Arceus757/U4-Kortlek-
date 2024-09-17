import random

# 1. Klass för kort
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __str__(self):
        return f"{self.rank}{self.suit}"

# 2. Klass för kortlek
class Deck:
    def __init__(self):
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        suits = ["♠", "♥", "♣", "♦"]
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]  # Skapar kortleken
    
    def show_all_cards(self):
        for card in self.cards:
            print(card)
    
    def draw_card(self):
        if self.cards:
            drawn_card = self.cards.pop(0)  # Tar bort och returnerar det första kortet
            print(f"Du drog: {drawn_card}")  # Visar vilket kort som drogs
            return drawn_card
        else:
            print("Kortleken är tom!")
            return None
    
    def shuffle(self):
        random.shuffle(self.cards)   

deck = Deck()           # Skapar kortlek
deck.shuffle()          # Blandar kortleken
deck.show_all_cards()   # Visar alla kort
deck.draw_card()        # Drar ett kort och visar det
