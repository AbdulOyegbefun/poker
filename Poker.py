#  File: Poker.py

#  Description: Teaching Python how to play Poker

#  Student Name: Abdulateef Oyegbefun

#  Student UT EID: Afo296

#  Partner Name: Jesus Marcos

#  Partner UT EID: Jam27482

#  Course Name: CS 313E

#  Unique Number: 52038

#  Date Created: 02/07/2022

#  Date Last Modified:02/09/2022

import random

class Card(object):
    RANKS = (2,3,4,5,6,7,8,9,10,11,12,13,14)

    SUITS = ('C','D','H','S')

    # constructor
    def __init__ (self, rank = 12, suit = 'S'):
        if (rank in Card.RANKS): 
            self.rank = rank
        else:
            self.rank = 12
        
        if (suit in Card.SUITS):
            self.suit = suit
        else:
            self.suit = 'S'

    # string representation of a Card object
    def __str__ (self):
        if (self.rank == 14):
            rank = 'A'
        elif(self.rank == 13):
            rank = 'K'
        elif(self.rank == 12):
            rank = 'Q'
        elif(self.rank == 11):
            rank = "J"
        else:
            rank = str(self.rank)
        return rank + self.suit
    
    # equality tests
    def __eq__(self, other):
        return self.rank == other.rank
    
    def __ne__(self, other):
        return self.rank != other.rank
    
    def __lt__(self, other):
        return self.rank < other.rank

    def __le__(self, other):
        return self.rank <= other.rank

    def __gt__(self, other):
        return self.rank > other.rank

    def __ge__(self, other):
        return self.rank >= other.rank

class Deck (object):
    # constructor
    def __init__ (self,num_decks=1):
        self.deck = []
        for i in range(num_decks):
            for suit in Card.SUITS:
                for rank in Card.RANKS:
                    card = Card(rank,suit)
                    self.deck.append(card)

     # shuffle the deck
    def shuffle (self):
        random.shuffle(self.deck)
    
    # deal a card
    def deal (self):
        if (len(self.deck) == 0):
            return None
        else:
            return self.deck.pop(0)

class Poker(object):
    def __init__ (self, num_players = 2, num_cards = 5):
        self.deck = Deck()
        self.deck.shuffle()
        self.all_hands = []
        self.numCards_in_Hand = num_cards    

        # deal all the cards
        for i in range (num_players):
            hand = []
            for j in range(self.numCards_in_Hand):
                hand.append (self.deck.deal()) 
            self.all_hands.append(hand)
        
    # simulate the play of the game
    def play (self):
        # sort the hands of each player and print
        for i in range(len(self.all_hands)):
            sorted_hand = sorted (self.all_hands[i], reverse = True)
            self.all_hands[i] = sorted_hand
            hand_str =''
            for card in sorted_hand:
                hand_str = hand_str + str(card) + ' '
            print('Player ' + str(i +1) + ": " + hand_str)

    # determine if a hand is a royal flush
    # takes as argument a list of 5 Card objects
    # returns a number of points for that hand

    def is_royal (self, hand):
        same_suit = True
        for i in range(len(hand)-1):
            same_suit = same_suit and (hand[i].suit) != (hand[i+1].suit)
            #if (hand[i].suit) != (hand[i+1].suit):
            #    return False
        
        if (not same_suit):
            return 0, ''
        
        rank_order = True
        for i in range(len(hand)):
            rank_order = rank_order and (hand[i].rank == 14 - i)
        
        if (not rank_order):
            return 0,''
        
        # determine the points
        points = 10 * 15**5 + \
            (hand[0].rank) * 15 ** 4 +\
            (hand[1].rank) * 15 ** 3 +\
            (hand[2].rank) * 15 ** 2 +\
            (hand[3].rank) * 15 ** 1 +\
            (hand[4].rank)
        return points, 'Royal Flush'


    def is_straight_flush(self,hand):
        same_suit = True
        for i in range(len(hand)-1):
            same_suit = same_suit and (hand[i].suit) != (hand[i+1].suit)
            #if (hand[i].suit) != (hand[i+1].suit):
            #    return False
        
        if (not same_suit):
            return 0, ''
        
        rank_order = True
        for i in range(len(hand)):
            first_card_rank = hand[0].rank
            # assuming strictly linear and no circular movement
            # for example 14,2,3,4,5
            if first_card_rank >=6:
                rank_order = rank_order and (hand[i].rank == first_card_rank - i)
        
        if (not rank_order):
            return 0,''
        
        # determine the points
        points = 9 * 15**5 + \
            (hand[0].rank) * 15 ** 4 +\
            (hand[1].rank) * 15 ** 3 +\
            (hand[2].rank) * 15 ** 2 +\
            (hand[3].rank) * 15 ** 1 +\
            (hand[4].rank)
        return points, 'Straight Flush'

    def is_four_kind(self,hand):
        rank_order = True
        list_of_ranks=[]
        for i in range(len(hand)):
            list_of_ranks.append(hand[i].rank)

        set_of_unique_ranks = set(list_of_ranks)
        if set_of_unique_ranks!=2:
            rank_order = False
        else:
            for i in set_of_unique_ranks:
                x=list_of_ranks.count(i)
                if x==4:
                    rank_order = True
                    break
        
        if (not rank_order):
            return 0,''
        
        # determine the points
        points = 8 * 15**5 + \
            (hand[0].rank) * 15 ** 4 +\
            (hand[1].rank) * 15 ** 3 +\
            (hand[2].rank) * 15 ** 2 +\
            (hand[3].rank) * 15 ** 1 +\
            (hand[4].rank)
        return points, 'Four of a Kind'


    def is_full_house(self,hand):
        rank_order = True
        list_of_ranks=[]
        for i in range(len(hand)):
            list_of_ranks.append(hand[i].rank)

        set_of_unique_ranks = set(list_of_ranks)
        if set_of_unique_ranks != 2:
            rank_order = False
        else:
            for i in set_of_unique_ranks:
                x=list_of_ranks.count(i)
                if x==3:
                    rank_order = True
                    break
        
        if (not rank_order):
            return 0,''
        
        # determine the points
        points = 7 * 15**5 + \
            (hand[0].rank) * 15 ** 4 +\
            (hand[1].rank) * 15 ** 3 +\
            (hand[2].rank) * 15 ** 2 +\
            (hand[3].rank) * 15 ** 1 +\
            (hand[4].rank)
        return points, 'Full House'
    def is_flush(self,hand):
        same_suit = True
        for i in range(len(hand)-1):
            same_suit = same_suit and (hand[i].suit) != (hand[i+1].suit)

        if (not same_suit):
            return 0, ''
        
        # determine the points
        points = 6 * 15**5 + \
            (hand[0].rank) * 15 ** 4 +\
            (hand[1].rank) * 15 ** 3 +\
            (hand[2].rank) * 15 ** 2 +\
            (hand[3].rank) * 15 ** 1 +\
            (hand[4].rank)
        return points, 'Flush'
    def is_straight(self,hand):
        rank_order = True
        for i in range(len(hand)):
            first_card_rank = hand[0].rank
            # assuming strictly linear and no circular movement
            # for example 14,2,3,4,5
            if first_card_rank >=6:
                rank_order = rank_order and (hand[i].rank == first_card_rank - i)
        
        if (not rank_order):
            return 0,''
        
        # determine the points
        points = 5 * 15**5 + \
            (hand[0].rank) * 15 ** 4 +\
            (hand[1].rank) * 15 ** 3 +\
            (hand[2].rank) * 15 ** 2 +\
            (hand[3].rank) * 15 ** 1 +\
            (hand[4].rank)
        return points, 'Straight'
    def is_three_kind(self,hand):
        rank_order = True
        list_of_ranks=[]
        for i in range(len(hand)):
            list_of_ranks.append(hand[i].rank)

        set_of_unique_ranks = set(list_of_ranks)
        if set_of_unique_ranks!=3:
            rank_order = False
        else:
            for i in set_of_unique_ranks:
                x=list_of_ranks.count(i)
                if x==3:
                    rank_order = True
                    break
        
        if (not rank_order):
            return 0,''
        
        # determine the points
        points = 4 * 15**5 + \
            (hand[0].rank) * 15 ** 4 +\
            (hand[1].rank) * 15 ** 3 +\
            (hand[2].rank) * 15 ** 2 +\
            (hand[3].rank) * 15 ** 1 +\
            (hand[4].rank)
        return points, 'Three of a Kind'
    def is_two_pair(self,hand):
        rank_order = True
        list_of_ranks=[]
        for i in range(len(hand)):
            list_of_ranks.append(hand[i].rank)

        set_of_unique_ranks = set(list_of_ranks)
        if set_of_unique_ranks!=3:
            rank_order = False
        else:
            for i in set_of_unique_ranks:
                x=list_of_ranks.count(i)
                if x==2:
                    count+=1
                    if count == 2:
                        rank_order = True
                        break
        
        if (not rank_order):
            return 0,''
        
        # determine the points
        points = 3 * 15**5 + \
            (hand[0].rank) * 15 ** 4 +\
            (hand[1].rank) * 15 ** 3 +\
            (hand[2].rank) * 15 ** 2 +\
            (hand[3].rank) * 15 ** 1 +\
            (hand[4].rank)
        return points, 'Two Pair'
    def is_one_pair(self,hand):
        rank_order = True
        list_of_ranks=[]
        for i in range(len(hand)):
            list_of_ranks.append(hand[i].rank)

        set_of_unique_ranks = set(list_of_ranks)
        if set_of_unique_ranks!=4:
            rank_order = False
        else:
            for i in set_of_unique_ranks:
                x=list_of_ranks.count(i)
                if x==2:
                    rank_order = True
                    break
        
        if (not rank_order):
            return 0,''
        
        # determine the points
        points = 2 * 15**5 + \
            (hand[0].rank) * 15 ** 4 +\
            (hand[1].rank) * 15 ** 3 +\
            (hand[2].rank) * 15 ** 2 +\
            (hand[3].rank) * 15 ** 1 +\
            (hand[4].rank)
        return points, 'One Pair'

    def is_high_card(self,hand):
        points = 1 * 15**5 + \
            (hand[0].rank) * 15 ** 4 +\
            (hand[1].rank) * 15 ** 3 +\
            (hand[2].rank) * 15 ** 2 +\
            (hand[3].rank) * 15 ** 1 +\
            (hand[4].rank)
        return points, 'High Card'
    

    



def main():
    # prompt the user to input the number of players
    num_players = int(input('Enter the number of players: '))
    while ((num_players < 2) or (num_players > 6)):
        num_players = int(input('Enter the number of players: '))
    # create the Poker object
    game = Poker(num_players)

    # play the game
    game.play()
    for i in range(len(game.all_hands)):
            print(game.is_royal(game.all_hands[i]))

    #game.is_royal()

main()
