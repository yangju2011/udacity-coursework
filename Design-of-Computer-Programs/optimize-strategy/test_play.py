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

def updates(state):
    return hold(state) if p == 0 else roll(state,random.randint(1, 6)) 

state = (0,0,0,0)
p,me,you,pending=state

while me < 10 and you < 10:
    state = updates(state)
    print updates(state)
    p,me,you,pending=state
    


# Notice that the functions 'always_hold' and 'always_roll' might not be doing exactly what you think they do.
# always_hold' holds even before the first roll.
# That is, when it has zero pending points, it refuses to roll, and therefore it always scores zero points.
# Not very clever, but that is the way it goes.
# 'always_roll' on the other hand, is almost as foolish.
# Even if it is lucky and has a pending score that is greater than the goal, it continues to roll until it pigs out.

'''def test():
    for _ in range(10):
        winner = play_pig(always_hold, always_roll)
        assert winner.__name__ == 'always_roll'
    return 'tests pass'

print test()'''

