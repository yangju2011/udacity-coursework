# -----------
# User Instructions
# 
# Write a function, deal(numhands, n=5, deck), that 
# deals numhands hands with n cards each.
#

import random # this will be a useful library for shuffling

# This builds a deck of 52 cards. If you are unfamiliar
# with this notation, check out Andy's supplemental video
# on list comprehensions (you can find the link in the 
# Instructor Comments box below).

mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC'] # 4*13=52 cards

def deal1(numhands, n=5, deck=mydeck):
    # Your code here.
    # return lists of numhands different hands
    # numhands: number of players (52/5=10+2, at most 10 ppl)
    maxnum = int(len(deck)/n)
    if numhands > maxnum:
        return Error
    else:
        # random.sample(population, k)
        # Return a k length list of unique elements chosen from the population sequence. Used for random sampling without replacement.
        hands = []
        i = 1
        while i <= numhands:
            hand = random.sample(deck,n)
            hands.append(hand)
            for x in hand:
                deck.remove(x) # remove will change the original deck
            i = i + 1
        return hands
        
    # this way After mydeck is consumed, even if another variable with the same name called mydeck is defined, it can not be recognized by deal. Because this new mydeck actually references to another address compared to the previous mydeck which is memorized by deal and consumed already. 
def deal(numhands, n=5, deck=mydeck):
    random.shuffle(deck)
    hands = []
    i = 0
    while i < numhands:
        hand = deck[i*n:(i+1)*n]
        hands.append(hand)
        i = i + 1
    return hands
    # return [deck[n*i:n*(i+1)] for i in range(numhands)]
    
print deal (10,5,mydeck)
print deal (10,5,mydeck)
