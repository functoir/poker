#!/usr/bin/env python3

from Deck import ( Deck, Card, Rank, Suit )

class Poker:
    
    def __init__(self, num_players=2):
        self.players = num_players
        self.deck = Deck()
        
        print(self.deck)
        
if __name__ == "__main__":
    game = Poker()
    del game
