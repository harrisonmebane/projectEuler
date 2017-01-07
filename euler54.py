# This program compares poker hands and returns the number of hands won by
# player one in the file poker.txt.

from collections import Counter

class Hand:

    straight_list = [
        [14,2,3,4,5],
        [2,3,4,5,6],
        [3,4,5,6,7],
        [4,5,6,7,8],
        [5,6,7,8,9],
        [6,7,8,9,10],
        [7,8,9,10,11],
        [8,9,10,11,12],
        [9,10,11,12,13],
        [10,11,12,13,14]
    ]

    def __init__(self):
        self.cards = []

    def get_cards(self):
        return self.cards

    def add_card(self,card):
        self.cards.append(card)

    def get_ranks(self):
        return map(lambda x: x.get_rank(),self.cards)

    def get_suits(self):
        return map(lambda x: x.get_suit(),self.cards)
    

class Card:

    card_dict = {'2':2,
                 '3':3,
                 '4':4,
                 '5':5,
                 '6':6,
                 '7':7,
                 '8':8,
                 '9':9,
                 'T':10,
                 'J':11,
                 'Q':12,
                 'K':13,
                 'A':14}

    def __init__(self,card):
        self.suit = self.parse_suit(card)
        self.rank = self.parse_rank(card)

    def parse_suit(self,card):
        return card[1]

    def parse_rank(self,card):
        return self.card_dict[card[0]]
                
    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

def main():

    hand_file = open("poker.txt","rb")
    
    sum = 0
    hands = hand_file.readline()
    while(hands):

        hand_list = hands[:-1].split(' ')

        hand1_list = hand_list[:5]
        hand2_list = hand_list[5:]

        hand1 = Hand()
        hand2 = Hand()

        for card_string in hand1_list:
            hand1.add_card(Card(card_string))

        for card_string in hand2_list:
            hand2.add_card(Card(card_string))

        hand1_rank = rank_hand(hand1)
        hand2_rank = rank_hand(hand2)

        if (hand1_rank > hand2_rank):
            sum += 1

        hands = hand_file.readline()
    
    print sum
    return

def rank_hand(hand):

    if (straight_flush(hand)):
        assert(type(straight_flush(hand))==int)
        rank = straight_flush(hand)
        return 8*15**5 + rank
    elif (four_of_a_kind(hand)):
        assert(len(four_of_a_kind(hand))==2)
        ranks = four_of_a_kind(hand)
        return 7*15**5 + compute_score(ranks)
    elif (full_house(hand)):
        assert(len(full_house(hand))==2)
        ranks = full_house(hand)
        return 6*15**5 + compute_score(ranks)
    elif (flush(hand)):
        assert(len(flush(hand))==5)
        ranks = flush(hand)
        return 5*15**5 + compute_score(ranks)
    elif (straight(hand)):
        assert(type(straight(hand))==int)
        rank = straight(hand)
        return 4*15**5 + rank
    elif (three_of_a_kind(hand)):
        assert(len(three_of_a_kind(hand))==3)
        ranks = three_of_a_kind(hand)
        return 3*15**5 + compute_score(ranks)
    elif (two_pair(hand)):
        assert(len(two_pair(hand))==3)
        ranks = two_pair(hand)
        return 2*15**5 + compute_score(ranks)
    elif (one_pair(hand)):
        assert(len(one_pair(hand))==4)
        ranks = one_pair(hand)
        return 15**5 + compute_score(ranks)
    else:
        ranks = hand.get_ranks()
        ranks.sort()
        zipped_ranks = zip(ranks,range(len(ranks)))
        return sum(map(lambda x: x[0]*(15**x[1]),zipped_ranks))

def straight_flush(hand):
    if (straight(hand) and flush(hand)):
        return straight(hand)
    else: 
        return False

def four_of_a_kind(hand):
    freq_dict = get_frequencies(hand,lambda x: x.get_ranks())
    freq_freq_dict = get_frequencies(freq_dict,lambda x: x.values())
    if (freq_freq_dict[4]==1):
        return map(lambda x: x[0], 
                   sorted(freq_dict.iteritems(),key=lambda x: (x[1],x[0])))
    else:
        return False

def full_house(hand):
    freq_dict = get_frequencies(hand,lambda x: x.get_ranks())
    freq_freq_dict = get_frequencies(freq_dict,lambda x: x.values())
    if (freq_freq_dict[3]==1 and freq_freq_dict[2]==1):
        return map(lambda x: x[0], 
                   sorted(freq_dict.iteritems(),key=lambda x: (x[1],x[0])))
    else:
        return False

def flush(hand):
    freq_dict = get_frequencies(hand,lambda x: x.get_suits())
    if (len(freq_dict.items())==1):
        return sorted(hand.get_ranks())
    else:
        return False

def straight(hand):
    ranks = sorted(hand.get_ranks())
    if ranks in hand.straight_list:
        return ranks[-1] if ranks[-1]<14 else ranks[-2]
    return False

def three_of_a_kind(hand):
    freq_dict = get_frequencies(hand,lambda x: x.get_ranks())
    freq_freq_dict = get_frequencies(freq_dict,lambda x: x.values())
    if (freq_freq_dict[3]==1 and freq_freq_dict[1]==2):
        return map(lambda x: x[0], 
                   sorted(freq_dict.items(),key=lambda x: (x[1],x[0])))
    else:
        return False

def two_pair(hand):
    freq_dict = get_frequencies(hand,lambda x: x.get_ranks())
    freq_freq_dict = get_frequencies(freq_dict,lambda x: x.values())
    if (freq_freq_dict[2]==2):
        return map(lambda x: x[0], 
                   sorted(freq_dict.items(),key=lambda x: (x[1],x[0])))
    else:
        return False

def one_pair(hand):
    freq_dict = get_frequencies(hand,lambda x: x.get_ranks())
    freq_freq_dict = get_frequencies(freq_dict,lambda x: x.values())
    if (freq_freq_dict[2]==1 and freq_freq_dict[1]==3):
        return map(lambda x: x[0], 
                   sorted(freq_dict.items(),key=lambda x: (x[1],x[0])))
    else:
        return False

def get_frequencies(hand,get_func):
    return Counter(get_func(hand))

def compute_score(rank_list):
    zipped_ranks = zip(rank_list,range(len(rank_list)))    
    return sum(map(lambda x: x[0]*(15**x[1]),zipped_ranks))

if __name__ == "__main__":

    main()
