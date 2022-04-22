##### Dev Assessment
## Deck of Playing Cards
### Implementation of Card Games in Python



#### Features

- A class that models playing  cards
- A class representing a deck of cards
- A class representing a hand of playing cards


### class Card

creating suits and rank arrays 
```python
suit = ["spades", "hearts", "diamonds", "clubs"]
rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
```
printing the card in human readable format
```python
def __str__(self):
        return '%s %s' % (Card.suits[self.suit], Card.rank[self.rank])
```
comparing the combination of the card
```python
def __lt__(self, other):
        if self.rank == other.rank:
            return self.suit < other.suit
        else:
            return self.rank < other.rank
```

### class Deck

Initialize the deck with 52 cards with random order
```python
def __init__(self):
        self.deck = []
        for suit in range(4):
            for rank in range(13):
                self.deck.append(Card(suit, rank))
        self.shuffle()
```
Add a card to the deck
```python
def add_card(self, card):
        self.deck.append(card)
```
Remove a card from the deck
```python
def remove_card(self):
        return self.deck.pop()
```
Function to shuffle
```python
def shuffle(self):
        random.shuffle(self.deck)
```
### class Hand

Initialize the hand and winnner count
```python
def __init__(self, label):
        self.deck = []
        self.label = label
        self.win_count = 0
```
Getting the winner count for the hand
```python
def win_count(self):
        return self.win_count
```
Incrementing the winner count for each win
```python
def round_winner(self):
        self.win_count = self.win_count + 1
```






