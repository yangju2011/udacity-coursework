# -----------------
# User Instructions
# 
# Write a function, bsuccessors(state), that takes a state tuple as input
# and returns a dictionary of {state:action} pairs.
#
# A state is a (here, there, t) tuple, where here and there are 
# frozensets of people (indicated by their times), and potentially
# the 'light,' t is a number indicating the elapsed time.
# frozenset is not mutable, can't append, add, remove

#
# An action is a tuple (person1, person2, arrow), where arrow is 
# '->' for here to there or '<-' for there to here. 
# When only one 
# person crosses, person2 will be the same as person one, so the
# action (2, 2, '->') means that the person with a travel time of
# 2 crossed from here to there alone.

# frozenset is hashable, therefore, {frozenset: value}

import itertools

def bsuccessors(state):
    """Return a dict of {state:action} pairs. A state is a (here, there, t) tuple,
    where here and there are frozensets of people (indicated by their times) and/or
    the 'light', and t is a number indicating the elapsed time. Action is represented
    as a tuple (person1, person2, arrow), where arrow is '->' for here to there and 
    '<-' for there to here."""
    
    here, there, t = state

    successors = {}

    light = frozenset(['light'])
    
    if 'light' in here:
        # here and there are frozensets of people (indicated by their times)
        #frozenset can't even do index
        
        ppl = here-light #ppl is a frozenset 
        transfer1 = itertools.combinations(ppl,1) #list of one person transfer, then p is (1,)
        for p in transfer1: # p is an item in the list
            p = p[0]
            t = t + p
            action = (p,p,'->')
            p = frozenset([p])
            transfer = p | light
            here = here - transfer 
            there = there | transfer 
            successors[(here,there,t)] = action

        if len(ppl)>1:    
            transfer2 = itertools.combinations(ppl,2)
            for ps in transfer1: # ps is a tuple (1,2)
                p1,p2 = ps
                t = t + max(p1,p2)
                action = (p1,p2,'->')
                ps= frozenset(ps)
                transfer = ps | light
                here = here - transfer 
                there = there | transfer 
                successors[(here,there,t)] = action
                
                # frozenset not mutable, has to create a new fronzen set to represent here

    else:
        ppl = there-light #ppl is a frozenset 
        transfer1 = itertools.combinations(ppl,1) #list of one person transfer, then p is (1,)
        for p in transfer1: # p is an item in the list
            p = p[0]
            t = t+p
            action = (p,p,'<-')
            p = frozenset([p])
            transfer = p | light
            there = there - transfer 
            here = here | transfer 
            successors[(here,there,t)] = action

        if len(ppl)>1:    
            transfer2 = itertools.combinations(ppl,2)
            for ps in transfer1: # ps is a tuple (1,2)
                p1,p2 = ps
                t = t + max(p1,p2)
                action = (p1,p2,'->')
                ps= frozenset(ps)
                transfer = ps | light
                there = there - transfer 
                here = here | transfer 
                successors[(here,there,t)] = action
    return successors

print bsuccessors((frozenset([1, 'light']), frozenset([]), 3))
print bsuccessors((frozenset([]), frozenset([2, 'light']), 0))

def test():

    assert bsuccessors((frozenset([1, 'light']), frozenset([]), 3)) == {
                (frozenset([]), frozenset([1, 'light']), 4): (1, 1, '->')}

    assert bsuccessors((frozenset([]), frozenset([2, 'light']), 0)) =={
                (frozenset([2, 'light']), frozenset([]), 2): (2, 2, '<-')}
    
    return 'tests pass'

print test()
