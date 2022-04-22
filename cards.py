# creating a class for implementing card, defining the rank and suit

class Card:
    suit = ["spades", "hearts", "diamonds", "clubs"]
    rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '%s %s' % (Card.suits[self.suit], Card.rank[self.rank])
    
    def __lt__(self, other):
        if self.rank == other.rank:
            return self.suit < other.suit
        else:
            return self.rank < other.rank

# creating the deck class, which will implement shuffled deck 
import random 
class Deck:
    def __init__(self):
        self.deck = []
        for suit in range(4):
            for rank in range(13):
                self.deck.append(Card(suit, rank))
        self.shuffle()
        
    def __len__(self):
        return len(self.deck)
    
    def add_card(self, card):
        self.deck.append(card)
        
    def remove_card(self):
        return self.deck.pop()
    
    def shuffle(self):
        random.shuffle(self.deck)


# creating the hand class which is an instance of deck for example 3 of spades 
class Hand(Deck):
    def __init__(self, label):
        self.deck = []
        self.label = label
        self.win_count = 0
        
    def __str__(self):
        return self.label + ': ' + ' '.join([str(card) for card in self.deck])
    
    def label(self):
        return self.label
    
    def win_count(self):
        return self.win_count
    
    def round_winner(self):
        self.win_count = self.win_count + 1
    
    def __str__(self):
        return "Card for " + self.label + " is " + Deck.__str__(self)