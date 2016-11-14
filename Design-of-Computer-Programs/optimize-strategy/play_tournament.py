''' optimal pig'''
other = {0:1,1:0}
actions = ['roll','hold']
goal = 40

import random

from functools import update_wrapper

def decorator(d):
    "Make function d a decorator: d wraps a function fn."
    def _d(fn):
        return update_wrapper(d(fn), fn)
    update_wrapper(_d, d)
    return _d

@decorator
def memo(f):
    """Decorator that caches the return value for each call to f(args).
    Then when called again with same args, we can just look it up."""
    cache = {}
    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = f(*args)
            return result
        except TypeError:
            # some element of args can't be a dict key
            return f(args)
    return _f


def roll(state,d):
    p, me, you, pending = state
    if d == 1:
        return (other[p],you, me+1,0) #swap me and you when other[p]
    else:
        return (p,me,you,pending+d) # random intergers 1-6

def hold(state):
    p, me, you, pending = state
    return (other[p],you,me+pending,0)


def pig_actions(state):
    _,_,_,pending = state
    return ['roll','hold'] if pending else ['roll']
    # if pending is None or 0, should roll, otherwise have 2 options


def Q_pig(state,action,Pwin): # expected U
    if action == 'roll':
        # if roll to 1, back to opponents turn, else, it is my turn /6
        return (1-Pwin(roll(state,1)) + sum(Pwin(roll(state,d)) for d in (2,3,4,5,6)))/6. # here should use 6. not 6 to get float number resuls during calculations
    if action == 'hold':
        # after i hold, it's opponents turn, and his state of winning 
        return 1 - Pwin(hold(state))
    raise ValueError

# utility function is the probability of winning
@memo #decorator here
def Pwin(state):
    p,me,you,pending = state
    if me+pending >= goal: # it is my turn, so only me+pending, not you+pending
        return 1
    elif you >= goal:
        return 0
    else: # otherwise, it is recursive function,
        return max(Q_pig(state,action,Pwin) for action in pig_actions(state))


def best_action(state, actions, Q, U):
    "Return the optimal action for a state, given U."
    def EU(action): return Q(state, action, U)
    return max(actions(state), key=EU)

def max_wins(state):
    return best_action(state, pig_actions, Q_pig, Pwin)

def play_tournament(s):
    # A,B are two strategies used by 2 people
    # means it takes in state and return action, A,B are functions
    N=len(s)
    state = N*(0,)
    while True:
        p, me, you, pending = state
        if me >= 50:
            return s[p] # at my turn
        elif: # at your turn, therefore your p
            return s[other[p]]
        elif strategies[p](state) == 'hold':
            state = hold(state)
        else:
            state = roll(state,random.randint(1,6))

strategies = [clueless, hold_at(goal/4),hold_at(1+goal/3),hold_at(goal/2),hold_at(goal),max_wins]

play_tournament(strategies)

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

    
