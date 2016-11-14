''' best strategies'''
'''Game theory with gamble'''

import math

def actions(state):
    return ['gamble','hold']

million = 1000000

def Q(state,action,U): # the outcome from a certain action
    # the expected value of taking action in a state, according to utility U
    if action == 'hold':
        return U(state + 1 * million)
    if action == 'gamble':
        return U((state + 3 * million)/2 + state/2)

# utility is defined as how much a certain outcome is valued
def utility(x):
    return math.log(x)

U = utility

print Q('hold',0,U)
print Q('gamble',0,U)
# 13.815510558
# 14.2209756661
# not that different then 

''' when linear
def test():
    assert outcome('hold',0) == 1000000
    assert outcome('gamble',0) == 1500000
    return 'tests pass'

print test()'''


# utility(state) --> number
# quality(state,action) --> number

def best_action(state,actions,Q,U):
    # return the optimal action for a state, given U, use action that has the highest expected utility
    
    def EU(action): return Q(state,action,U)
    return max(actions(state),key=EU)
    
print best_action(0,actions,Q,U)
print best_action(100*million,actions,Q,U)
