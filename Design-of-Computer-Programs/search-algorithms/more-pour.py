# -----------------
# User Instructions
# 
# In this problem, you will solve the pouring problem for an arbitrary
# number of glasses. Write a function, more_pour_problem, that takes 
# as input capacities, goal, and (optionally) start. This function should 
# return a path of states and actions.
#
# Capacities is a tuple of numbers, where each number represents the 
# volume of a glass. 
#
# Goal is the desired volume and start is a tuple of the starting levels
# in each glass. Start defaults to None (all glasses empty).
#
# The returned path should look like [state, action, state, action, ... ]
# where state is a tuple of volumes and action is one of ('fill', i), 
# ('empty', i), ('pour', i, j) where i and j are indices indicating the 
# glass number. 



def more_pour_problem(capacities, goal, start=None):
    """The first argument is a tuple of capacities (numbers) of glasses; the
    goal is a number which we must achieve in some glass.
    start is a tuple of starting levels for each glass; if None, that means 0 for all.

    Start at start state and follow successors until we reach the goal.
    
    Keep track of frontier and previously explored; fail when no frontier.
    
    On success return a path: a [state, action, state2, ...] list

    where an action is one of ('fill', i), ('empty', i), ('pour', i, j), where
    i and j are indices indicating the glass number."""
    # your code here
    if start == None:
        n = len(capacities)
        start_state = (0,)*n # n * 0
    else:
        start_state = start
    return shortest_path_search(start_state, psuccessors, is_goal,goal,capacities)

def psuccessors(state,capacities): # state is a tuple (1,2,3,4) for current value, capacity is also a tuple, capacity[0]-capacity[n]
    n = len(state)
    outs = {}
    for i in range(n):
        emptyi= state[:i]+(0,)+state[i+1:]
        outs[emptyi]= ('empty',i) #state[i] = 0, but list is not hashble
        filli = state[:i]+(capacities[i],)+state[i+1:]
        outs[filli]=('fill',i)
    for i in range(n):
        for j in range(n):
            if j > i:
                if state[i]+state[j] > capacities[j]:
                    pourij = state[:i]+((state[i]+state[j]-capacities[j]),)+state[i+1:j]+(capacities[j],)+state[j+1:]
                else:
                    pourij = state[:i]+(0,)+state[i+1:j]+((state[i]+state[j]),)+state[j+1:]
                outs[pourij] = ('pour', i, j)
            if i > j:
                if state[i]+state[j] > capacities[j]:
                    pourij = state[:j]+ (capacities[j],)+ state[j+1:i]+((state[i]+state[j]-capacities[j]),)+state[i+1:]
                else:
                    pourij = state[:j]+((state[i]+state[j]),)+ state[j+1:i]+(0,)+state[i+1:]
                outs[pourij] = ('pour', i, j)
    return outs
        
    
def is_goal(state,goal):
    if goal in state:
        return True
    else:
        return False

    # if define is_goal inside the outer function, we then do not need to include goal in the is_goal function :)
    
def shortest_path_search(start, successors, is_goal, goal, capacities):
    """Find the shortest path from start state to a state
    such that is_goal(state) is true."""
    if is_goal(start,goal):
        return [start]
    explored = set()
    frontier = [ [start] ] 
    while frontier:
        path = frontier.pop(0)
        s = path[-1]
        for (state, action) in successors(s,capacities).items():
            if state not in explored:
                explored.add(state)
                path2 = path + [action, state]
                if is_goal(state,goal):
                    return path2
                else:
                    frontier.append(path2)
    return Fail

Fail = []


def test_more_pour():
    assert more_pour_problem((1, 2, 4, 8), 4) == [
        (0, 0, 0, 0), ('fill', 2), (0, 0, 4, 0)]
    assert more_pour_problem((1, 2, 4), 3) == [
        (0, 0, 0), ('fill', 2), (0, 0, 4), ('pour', 2, 0), (1, 0, 3)] 
    starbucks = (8, 12, 16, 20, 24)
    assert not any(more_pour_problem(starbucks, odd) for odd in (3, 5, 7, 9))
    assert all(more_pour_problem((1, 3, 9, 27), n) for n in range(28))
    assert more_pour_problem((1, 3, 9, 27), 28) == []
    return 'test_more_pour passes'

print test_more_pour()
