# -----------------
# User Instructions
# 
# Write a function, play_pig, that takes two strategy functions as input,
# plays a game of pig between the two strategies, and returns the winning
# strategy. Enter your code at line 41.
#
# You may want to borrow from the random module to help generate die rolls.

import random

possible_moves = ['roll', 'hold']
other = {1:0, 0:1}
goal = 50

def clueless(state):
    "A strategy that ignores the state and chooses at random from possible moves."
    return random.choice(possible_moves)

def hold(state):
    """Apply the hold action to a state to yield a new state:
    Reap the 'pending' points and it becomes the other player's turn."""
    (p, me, you, pending) = state
    return (other[p], you, me+pending, 0)

def roll(state, d):
    """Apply the roll action to a state (and a die roll d) to yield a new state:
    If d is 1, get 1 point (losing any accumulated 'pending' points),
    and it is the other player's turn. If d > 1, add d to 'pending' points."""
    (p, me, you, pending) = state
    if d == 1:
        return (other[p], you, me+1, 0) # pig out; other player's turn
    else:
        return (p, me, you, pending+d)  # accumulate die roll in pending

def play_pig(A, B):
    """Play a game of pig between two players, represented by their strategies.
    Each time through the main loop we ask the current player for one decision,
    which must be 'hold' or 'roll', and we update the state accordingly.
    When one player's score exceeds the goal, return that player."""
    # your code here, state:action, action is strategy, state has the number for score, strategy returns an action
    #2 players take turn to do it, 0 represents A, 1 represents B
    
   
    '''def suc_A(state):
        return hold(state) if A(state)=='hold' else roll(state,random.randint(1, 6))
        
    def suc_B(state):
        return hold(state) if B(state)=='hold' else roll(state,random.randint(1, 6)) 

    # return a succesor state from a certain action

    def updates(state):
        return suc_A(state) if p == 0 else suc_B(state)

    p,me,you,pending = state # tuple number can't be changed, updates state
    i = 0
    while me < goal and you < goal:
        state = updates(state)
        p,me,you,pending = state # update state, not return state1
        i = i+1

    #(0,0,50,0),at this step, reached 50, one number is no 5

    return B if you>=goal else A'''

    strategies = [A,B]
    p,me,you,pending = state= (0,0,0,0)
    while True:
        if me >= goal:
            return strategies[p] # use strategies[p] to index different strategies
        elif you >= goal:
            return strategies[other[p]]
        elif strategies[p](state) == 'hold':
            state = hold(state)
        elif strategies[p](state) == 'roll':
            state = roll(state, random.randint(1, 6))
        p,me,you,pending = state #  update me and you
    

def always_roll(state):
    return 'roll'

def always_hold(state):
    return 'hold'

# Notice that the functions 'always_hold' and 'always_roll' might not be doing exactly what you think they do.
# always_hold' holds even before the first roll.
# That is, when it has zero pending points, it refuses to roll, and therefore it always scores zero points.
# Not very clever, but that is the way it goes.
# 'always_roll' on the other hand, is almost as foolish.
# Even if it is lucky and has a pending score that is greater than the goal, it continues to roll until it pigs out.

def test():
    for _ in range(10):
        winner = play_pig(always_hold, always_roll)
        assert winner.__name__ == 'always_roll'
    return 'tests pass'

print test()

