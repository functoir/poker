#!/usr/bin/env python3

from poker_utils import ( Deck, Card, Rank, Suit )

class Poker:
    
    def __init__(self, num_players=2):
        self.players = num_players
        self.__deck = Deck()
        print(self.__deck)
        
        print(self.__deck)
        
if __name__ == "__main__":
    game = Poker()
    game.__deck.shuffle()
    print(game.__deck)
    
    del game
