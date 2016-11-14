
'''
successors and search function
key concepts:
1. goal
2. start ()
3. succesor function
-- {state:action}

final output
path = [state,action,state,action,state...]

find path
1. shortest path: least step
2. least cost, add a factor of time/cost to calculate action_cost and total_cost

'''

# output of successors is {state:action}
# for cost optimization, {state:(action,action_cost)} but action_cost is not stored in paths
# action is usually a string describing how to get to successor states
# cost can be time, or other, usually a number for comparision 

    
def find_shortest_path(start, successor, is_goal):
    if is_goal(start):
        return [start]
    else:
        explored = set() # a set of explored states, explored means successors of this state is calculated
        frontier = [[start]] # a list of paths
        while frontier:
            path = frontier.pop(0) # replace path with path 2
            s = path[-1]
            
            successors = successor(s) # a dict of {state:action} --> a list of tuple (state,action)
            explored.add(s)
            
            for (state,action) in successors.items():
                if state not in explored: # not to repeat
                    path2 = path + [action,state]
                    # ??? explored.add(state) ???

                    if is_goal(state): # successor state is is_goal, but not yet explored for its later successors
                        return path2
                    else:
                        frontier.append(path2)
        return Fail          
                
Fail = []

def find_cheapest_path(start, successor, is_goal,action_cost):
    if is_goal(start):
        return [start]
    else:
        explored = set() # a set of explored states, explored means successors of this state is calculated
        frontier = [[start]] # a list of paths


        while frontier:
                   
            path = frontier.pop(0) # replace path with path 2
            state1 = final_state(path) #final_state

            if is_goal(state1): # successor state is is_goal, but not yet explored for its later successors
                return path
            
            total_cost = path_cost(path)
            
            successors = successor(state1) # a dict of {state:action} --> a list of tuple (state,action)
            explored.add(state1)
            
            for (state,action2) in successors.items():
                
                action_cost = action2[1]                
                total_cost = total_cost + action_cost(action)
                action = action2[0]
                path2 = path + [(action,total_cost),state]
                add_to_frontier(path2) #replacing costlier path if there is one.

                
        return Fail = []          

def add_to_frontier(frontier,path):
    old = None
    for i,p in enumerate(frontier): #index frontier for deletion
        if final_state(p) == final_state(path):
            old = i
            break
    if old is not None and path_cost(frontier[old]) < path_cost(path):
        return
    elif old is not None:
        del frontier[old]

    frontier.append(path)
    frontier.sorted(key=path_cost)
    


def final_state(path):
    return path[-1]
    








    

    
def path_cost(path): # element of frontier 
    if len(path) < 3:
        return 0 # no action taken
    else:
        action, total_cost = path[-2]
        return total_cost # path[-2][1]
    
def successor(state):
    return {state: action}

                
def path_states(paths):
    return paths [0::2]

def path_actions(paths):
    return paths [1::2]

def is_goal(state,):
    if state == goal: #goal is a given number
        return True
    else:
        return False
