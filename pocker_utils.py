#!/usr/bin/env python3

import random
from enum import IntEnum
import Numba

class Suit(IntEnum):
    Clubs = 0
    Diamonds = 1
    Spades = 2
    Hearts = 3
    
    def __str__(self):
        return self.name

class Rank(IntEnum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    
    def __str__(self):
        return self.name

class Card:
    
    def __init__(self, number: int, suit: int):
        self.rank = Rank(number)
        self.suit = Suit(suit)

    def __str__(self):
        return f"{self.rank.name} of {self.suit.name}"

class Deck:

    def __init__(self):
        self.cards = []
        for rank in Rank:
            for suit in Suit:
                card = Card(rank, suit)
                self.cards.append(card)
                
    def __str__(self):
        return "\n".join([str(card) for card in self.cards])
                
    
    def pop(self):
        return self.cards.pop()
        

    def random(self):
        index = random.randint(0, len(self.cards))
        card = self.cards[index]
        return str(card)

    def shuffle(self, swaps=1000):
        last_index = len(self.cards)-1
        for _ in range(swaps):
            source_index = random.randint(0, last_index)
            dest_index = random.randint(0, last_index)
            self.swap(self.cards, source_index, dest_index)

    @staticmethod
    def swap(array, a, b):
        temp = array[a]
        array[a] = array[b]
        array[b] = temp
        
    def reset(self):
        self.__init__()
        
    def __iter__(self):
        return iter(self.cards)
    
    def __getitem__(self, index):
        return self.cards[index]
    
    def __len__(self):
        return len(self.cards)
    
    def __bool__(self):
        return bool(self.cards)
        
if __name__ == "__main__":

    deck = Deck()
    
    print("Five random cards in the deck.\n")
    for i in range(5):
        print(deck.random())
        
    print("\n\nFirst five:\n\n")
    for i in range(5):
        print(deck[i])
        
    print("\nShuffling the deck, 10 swaps allowed.\n")
    deck.shuffle(swaps=10)
    
    print("\n\nFirst five:\n\n")
    for i in range(5):
        print(deck[i])
        
    print("\n\nResetting the deck.\n\n")
    deck.reset()
    
    print("\n\nFirst five:\n\n")
    for i in range(5):
        print(deck[i])
        
    print("Shuffling the deck, 1000 swaps allowed.\n")
    deck.shuffle()
    
    print("\n\nFirst five:\n\n")
    for i in range(5):
        print(deck[i])
        
    print(len(deck))
    print("\n\n All cards in the deck:\n\n")
    while deck:
        print(deck.pop())
        
    print(len(deck))
  