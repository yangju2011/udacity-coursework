# hands is a list of different hands, each hand has 5 cards with number + suit
# each hand is written in a string 'AH 2S 3B JC KC'
# use each hand as a list by hand.split() -- > ['AH','2S'..]


def poker(hands):
    return max(hands,key=hand_rank)
# to handle tie, instead of max(hand), define allmax, equal to max, then return it too 
    
# hand is a list of cards with both number and suit
def hand_rank(hand):
    rank = card_rank(hand)
    if straight(rank) and flush(hand):
        return (8,max(rank)) # highest card_rank
    if kind(4,rank):
        return (7, kind(4,rank),kind(1,rank))
    if kind(3,rank) and kind(2,rank):
        return (6,kind(3,rank),kind(2,rank))
    if flush(hand):
        return (5,rank)
    if straight(rank):
        return (4,max(rank))
    if kind(3,rank):
        return (3, kind(3,rank), rank)
    if two_pair(rank):
        return (2,kind(2,rank),kind(2,sorted(rank)),kind(1,rank)) # kind(2,rank) returns the largest kind2
    # sorted (rank) to return the small kind2
    if kind(2,rank):
        return (1,kind(2,rank),rank)
    else:
        return(0, rank)

def card_rank(hand):
    strrank = [r for r,s in hand]
    # translate string 'A23' to int 14, 2, 3
    rank = ['--23456789TJQKA'.index(r) for r in strrank]
    # could also use string.find(r)
    
    # if sorted, and then return, won't produce sorted arnk from big to small
    return sorted(rank,reverse=True)
    # a list in int, and sorted from biggest to smallest

def straight(rank): # if a rank is given as a sorted list of ints
    # A2345 is also considered as straight
    # instead write if A return True, simply return statement A
    return (len(set(rank)) == 5 and (max(rank)-min(rank)) == 4) or rank == [14,5,4,3,2]


def flush(hand): # check if all suits are the same
    return len(set([s for r,s in hand])) == 1
    '''if len(set([s for r,s in hand])) == 1:
        return True
    else:
        return False'''
    
def kind(n,rank): # x of a kind, list.count(obj) -- > int # return the number of the hand
    for r in rank:
        if rank.count(r) == n:
            return r
    return False

def two_pair(rank):
    return len(set(rank)) == 3 and not kind(3,rank)
                
def test():
    sf = ['7S','8S','5S','4S','6S']
    fk = ['5C','5S','5H','5D','9S']
    fh = ['KH','KD','KS','4C','4S']
    fl = ['KS','JS','3S','7S','9S']
    st = ['9S','8H','TD','7C','6H']
    thk =['5C','9S','QH','QS','QC']
    tp = ['JS','JC','9S','QH','QS']
    op = ['9H','6S','4C','AC','AD']
    hc = ['2C','3S','5D','7H','AD']

    assert card_rank(sf) == [8,7,6,5,4]
    assert straight(card_rank(sf)) == True
    assert straight(card_rank(fk)) == False
    assert flush(sf) == True
    assert kind(4,card_rank(fk)) == 5
    assert kind(4,card_rank(sf)) == False
    assert kind(4,card_rank(fh)) == False
    assert kind(3,card_rank(fh)) == 13
    assert kind(2,card_rank(fh)) == 4
    
    assert hand_rank(sf) == (8,8)
    assert hand_rank(fk) == (7,5,9)
    assert hand_rank(fh) == (6,13,4)
    assert hand_rank(fl) == (5,[13,11,9,7,3])
    assert hand_rank(st) == (4,10)
    assert hand_rank(thk) == (3,12,[12,12,12,9,5])
    assert hand_rank(tp) == (2,12,11,9)
    assert hand_rank(op) == (1,14,[14,14,9,6,4])
    assert hand_rank(hc) == (0,[14,7,5,3,2])

    assert two_pair(card_rank(tp)) == True
    assert two_pair(card_rank(fk)) == False

    # handle Ace straight
    ace = ['AB','2C','3C','4D','5H']
    assert straight(card_rank(ace))== True

    hands = [sf,fk,fh,fl,st,thk,tp,op,hc]
    assert poker(hands) == sf
    assert poker([thk,hc]) == thk
    
    return True

print test()
