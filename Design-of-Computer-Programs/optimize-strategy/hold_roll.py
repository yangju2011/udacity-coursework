# -----------------
# User Instructions
# 
# Write the two action functions, hold and roll. Each should take a
# state as input, apply the appropriate action, and return a new
# state. 
#
# States are represented as a tuple of (p, me, you, pending) where
# p:       an int, 0 or 1, indicating which player's turn it is.
# me:      an int, the player-to-move's current score
# you:     an int, the other player's current score.
# pending: an int, the number of points accumulated on current turn, not yet scored

def hold(state):
    """Apply the hold action to a state to yield a new state:
    Reap the 'pending' points and it becomes the other player's turn."""
    # your code here
    p, me, you, pending = state
    # has nothing to do with p number
    # only operates pending on me, which is the player to move
    if p == 1: # means it is my turn
        p1 = 0
    else: # means it is still myturn,
        p1 = 1
    return (other[p],you,me+pending,0)

other = {1:0,0:1} #mapping from player to other player, it is a dictionary, other[1] = 0, other[0]= 1
        
        
def roll(state, d):
    """Apply the roll action to a state (and a die roll d) to yield a new state:
    If d is 1, get 1 point (losing any accumulated 'pending' points),
    and it is the other player's turn. If d > 1, add d to 'pending' points."""
    # your code here
    p, me, you, pending = state
    if d == 1: #exchange
        pending1 = 0
        you1 = me+1
        me1 = you
        # return (other[p],you,me+1,0), reduce the line more compact
        if p == 1: # means it is my turn
            p1 = 0
        else: # means it is still myturn,
            p1 = 1
    else:
        you1 = you
        me1 = me #keeps on rolling
        pending1= pending+d
        p1 = p
        # return (p,me,you,pending+d)
    return (p1,me1,you1,pending1)
            
print hold((1, 10, 20, 7))  
print hold((0, 5, 15, 10))   
print roll((1, 10, 20, 7), 1) 
print roll((0, 5, 15, 10), 5)  

def test():    
    assert hold((1, 10, 20, 7))    == (0, 20, 17, 0)
    assert hold((0, 5, 15, 10))    == (1, 15, 15, 0)
    assert roll((1, 10, 20, 7), 1) == (0, 20, 11, 0)
    assert roll((0, 5, 15, 10), 5) == (0, 5, 15, 15)
    return 'tests pass'

print test()
