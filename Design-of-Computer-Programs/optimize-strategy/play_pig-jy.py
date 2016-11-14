'''
play pig with die rolls, 2 people take turns to hold or roll with pending numbers
whoever get 50 first wins.

each state for each round is defined as (p,me,you,pending)

me: the person to roll the die or make a decision
you: the other person
p: 2 people take turn, use 0,1,2,3 to mark which person

if roll to 1, pig out
else, can add to pending

'''

other = {0:1,1:0}
actions = ['roll','hold']
goal = 50

import random

# strategies 
def clueless(state):
    return random.choice(actions)

def all_roll(state): # A
    return 'roll'

def all_hold(state): # B
    return 'hold'

def hold_at(x): #x<=goal
    def action(state):
        p, me, you, pending = state
        return 'hold' if me + pending>=x else 'roll'
    return action   

def roll(state,d):
    p, me, you, pending = state
    if d == 1:
        return (other[p],you, me+1,0) #swap me and you when other[p]
    else:
        return (p,me,you,pending+d) # random intergers 1-6

def hold(state):
    p, me, you, pending = state
    return (other[p],you,me+pending,0)


def play_pig(A,B):
    # A,B are two strategies used by 2 people
    # means it takes in state and return action, A,B are functions
    strategies = [A,B]
    state = (0,0,0,0)
    while True:
        p, me, you, pending = state
        if me >= 50:
            return strategies[p] # at my turn
        elif: # at your turn, therefore your p
            return strategies[other[p]]
        elif strategies[p](state) == 'hold':
            state = hold(state)
        else:
            state = roll(state,random.randint(1,6))

    '''while me < goal and you <goal:
        if strategies[p](state) == 'hold':
            state = hold(state)
        else:
            state = roll(state,random.randint(1,6))
        p, me, you, pending = state
        
    # print state (1,0,50,0)
    if me >= 50:
        return strategies[p] # at my turn
    else: # at your turn, therefore your p
        return strategies[other[p]]'''

def test():
    assert hold((0,0,0,1)) == (1,0,1,0)
    assert hold((1,5,3,6)) == (0,3,11,0)
    assert roll((0,4,7,6),1) == (1,7,5,0)
    assert roll((1,5,6,3),5) == (1,5,6,8)
    assert hold_at(5)((0,1,3,4)) == 'hold'
    assert hold_at(5)((0,5,3,0))== 'hold'
    assert hold_at(15)((0,1,3,4)) == 'roll'

    winner = play_pig(all_roll,all_hold)
    assert winner.__name__ == 'all_roll'
    
    return 'tests pass'

print test()

