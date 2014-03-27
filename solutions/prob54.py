#!/usr/bin/python
import re
import random
import time

class BadCard(Exception): pass
class BadHand(Exception): pass

class Card:
    def __init__(self, value, suit):
        try:
            if (re.match('([2-9jJqQkKaA]|10)',value) != None and\
                    re.match('[sScChHdD]',suit) != None ):
                self.s = suit.upper()
                if(re.match("([2-9]|10)",value)): self.v = int(value)-2
                elif(re.match('[jJ]',value)): self.v = 9
                elif(re.match('[qQ]',value)): self.v = 10
                elif(re.match('[kK]',value)): self.v = 11
                elif(re.match('[aA]',value)): self.v = 12
                else:
                    print "Couldnt figure out a value for ", value
                    raise BadCard
            else:
                print "bad card with string value", value, "  and suit", suit
                raise BadCard
        except TypeError:
            if(value >= 0 and value <= 12 and\
                    re.match('[sScChHdD]',suit) != None):
                self.s = suit.upper()
                self.v = value
            else:
                print "bad card with int value", value, "  and suit", suit
                raise BadCard

    def __str__(self):
        string = ""
        if self.v == 9: string += "J"
        elif self.v == 10: string += "Q"
        elif self.v == 11: string += "K"
        elif self.v == 12: string += "A"
        else: string += str(self.v+2)
        return string + self.s

class Deck:
    def __init__(self):
        self.reinit()

    def reinit(self):
        deck = []
        counter = 0
        for v in range(0,13):
            for s in ["S","C","H","D"]:
                deck += [Card(v,s)]
                counter += 1
        random.shuffle(deck)
        self.d = deck

    def pop_card(self):
        return self.d.pop()

    def pop_hand(self):
        cards = []
        for i in range(0,5):
            cards += [self.d.pop()]
        return Hand(cards)

    def __str__(self):
        if len(self.d) == 0: return "Empty deck!!"
        else: string = ""
        i = 0
        for card in self.d:
            string += "Card " + str(i) + ":  " + str(card) + "\n"
            i += 1
        return string


class Hand:
    def __init__(self, cards):
        self.ranks = {\
                "high card": 0,\
                "one pair": 1,\
                "two pairs": 2,\
                "three of a kind": 3,\
                "straight": 4,\
                "flush": 5,\
                "full house": 6,\
                "four of a kind": 7,\
                "straight flush": 8,\
                "royal flush": 9}
        self.current_rank = 0
        if len(cards) == 5:
            self.c = cards
            s = []
            v = []
            for card in cards:
                s += [card.s]
                v += [card.v]
            self.s = sorted(s)
            self.v = sorted(v)

        else:
            print cards
            print "Tried to make a hand of size", len(cards)
            raise BadHand


    def set_rank(self, new_rank):
        if self.ranks[new_rank] > self.current_rank:
            self.current_rank = self.ranks[new_rank]

    def rank(self):
    # determines the highest value hand that can be made from these cards
        def remove_duplicates(self, l):
            return list(set(l))

        important_cards = []

        def check_flush(self):
            for s in ["S", "C", "H", "D"]:
                if self.s.count(s) == 5: return true
            return false

        def check_straight(self):
            sorted_v = sorted(self.v)
            if sorted_v == range(sorted_v[0],sorted_v[0]+5): return true
            return false

        def check_straight_flush(self):
            return (self.check_straight() and self.check_flush())

        def check_royal_flush(self):
            if self.check_straight_flush:
                try:
                    self.v.index(12)
                    return true
                except ValueError:
                    return false

        def check_four_of_a_kind(self):
            v = self.remove_duplicates(self.v)
            for value in v:
                if v.count(value) == 4: return true
            return false

        def check_full_house(self):
            v = self.remove_duplicates(self.v)
            triple = False
            pair = False
            for value in v:
                if v.count(value) == 3: triple = True
                elif v.count(value) == 2: pair = True
            return ( triple and pair )

        def check_three_of_a_kind(self):
            v = self.remove_duplicates(self.v)
            for value in v:
                if v.count(value) == 3: return true
            return false

        def check_two_pair(self):
            v = self.remove_duplicates(self.v)
            one_pair = False
            for value in v:
                if v.count(value) == 2:
                    if one_pair: return true
                    else: one_pair == True
            return false

        def check_one_pair(self):
            v = self.remove_duplicates(self.v)
            for value in v:
                if v.count(value) == 2: return true
            return false



#       for s in ["S", "C", "H", "D"]:
#           if self.s.count(s) == 5:
#               # some kind of flush
#               self.set_rank("flush")
#               if self.v == range(self.v[0],self.v[0]+5):
#                   # straight flush
#                   self.set_rank("straight flush")
#                   print "found a straight flush!", self, self.current_rank
#                   if self.v[-1] == 12:
#                       # royal straight flush
#                       self.set_rank("royal flush")
#                       print "found a royal straight flush!", self, self.current_rank
#       if(self.current_rank < self.ranks['straight'] and\
#               self.v == range(self.v[0],self.v[0]+5)):
#           # some kind of straight
#           self.set_rank("straight")
#       for v in set(self.v):
#           if self.v.count(v) == 4:
#               # 4 of a kind
#               self.set_rank("four of a kind")
#               print "found four of a kind!", self, self.current_rank
#           elif self.v.count(v) == 3:
#               # 3 of a kind
#               if self.current_rank == self.ranks['one pair']:
#                   self.set_rank("full house")
#                   print "found a full house!", self, self.current_rank
#               else:
#                   self.set_rank("three of a kind")
#           elif self.v.count(v) == 2:
#               # one pair
#               if self.current_rank == self.ranks['one pair']:
#                   self.set_rank("two pairs")
#               elif self.current_rank == self.ranks['three of a kind']:
#                   self.set_rank("full house")
#                   print "found a full house!", self, self.current_rank
#               else:
#                   self.set_rank("one pair")

    def __str__(self):
        string = "["
        for card in self.c:
            string += str(card) + ", "
        string = string[:-2] + "]"
        return string

class Round:
    def __init__(self, player_one_hand, player_two_hand):
        self.h1 = player_one_hand
        self.h2 = player_two_hand

    def determine_winner(self):
        pass


def generate_random_card():
    s = ['S','C','H','D']
    r1 = random.randint(1,4*4*12*12)
    r2 = random.randint(1,4*4*12*12)
    return Card((r1%12),s[r2%4])

def generate_random_hand():
    cards = []
    for i in range(0,5):
        cards += [generate_random_card()]
    return Hand(cards)




def main():
    try:
        d = Deck()
        while(True):
            p1 = d.pop_hand()
            p1.rank()
            p2 = d.pop_hand()
            p2.rank()
            d.reinit()
            print p1, p1.current_rank, p2, p2.current_rank
            time.sleep(0.2)
    except BadCard:
        print "bad card"
    except BadHand:
        print "bad hand"

if __name__ == '__main__':
    main()
