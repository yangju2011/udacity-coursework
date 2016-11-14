'''bucket problem
bucket 6, 9 oz
final target 4 oz
tap water tank
action
fill, empty, transfer
'''

def fillbucket(X,Y,goal,state = (0,0)):
# X,Y are capacity, goal is final numer to acheive, state is the current value in bucket
# return the path to achieve the goal, a series of states, imuatble tuple
# goal is a number

    if goal in state:
        return [state] #only state, no actions
    
    '''elif goal == X:
        return [(X,0)]
    
    elif goal == Y:
        return [(0,Y)]'''
    

    explored = set() # set of states, ((),(),()), not to repeat
    
    frontier = [[state]] #[[(0, 0)]] # ordered list of paths, not only the states, but also the paths to achieve such as states
    # path = [(),(),()]

    # the very last item is the frontier state
    
    while frontier:
        
        path = frontier.pop(0) # path is a list, shortes path first

            # print toexplore, (0, 0)
            
            # pop() is used it removes last element in your list
            # where as pop(0) means it removes the element in the index that is first element of the list
            
        to_explore_state = path[-1] # the last item of path is a (), from one state to the next 
        
        (x,y) = to_explore_state
        
        if to_explore_state not in explored:
            successors = successor(x,y,X,Y) # a dictionary
            explored.add(to_explore_state)

            for (state,action) in successors.items():
                # The method items() returns a list of dict's (key, value) tuple pairs
                # [((3,4),'X-->Y'),(),()]
                
                if state not in explored: # not to reverse
                    
                    path2 = path + [action,state] # [(0,0),'fill X', (6,0), 'x<-Y', (7,2)]

                    if goal in state:
                        return path2

                    else:
                        frontier.append(path2)
                    

    return [] # if notthing returned from the loop
        
def successor(x,y,X,Y):
    # return a dict of {state:action} to decribe what can be reached from the (x,y) state and how    

    assert x<=X and  y<=Y
    # make sure it even makes sense
    
    # for x bucket
    emptyx = (0,y)
    
    fillx = (X,y)
    
    # for y bucket
    emptyy = (x,y)

    filly = (x,Y)
    
    # transfer x to y
    if x+y > Y:
        t_x_to_y = (x+y-Y,Y)
    else:
        t_x_to_y = (0,x+y)

    
    # trasnfer y to x
    if x+y > X:
        t_y_to_x = (X, x+y-X)
    else:
        t_y_to_x = (x+y,0)

    outs = {emptyx: 'empty,X', fillx: 'fill X', emptyy: 'empty Y' , filly: 'fill Y' ,t_x_to_y: 'X->Y' ,t_y_to_x: 'Y->X'}
    # need to know how to get there 

    return outs

    # need to label the actual procedure by dictionaty 

    
def test():
    # print fillbucket(0,6,9,state = (0,0))
    print fillbucket(7,9,8)
    print fillbucket(9,8,2)
    # [(0, 0), 'fill Y', (0, 9), 'Y->X', (7, 2), 'empty,X', (0, 2), 'Y->X', (2, 0), 'fill Y', (2, 9), 'Y->X', (7, 4), 'empty,X', (0, 4), 'Y->X', (4, 0), 'fill Y', (4, 9), 'Y->X', (7, 6), 'empty,X', (0, 6), 'Y->X', (6, 0), 'fill Y', (6, 9), 'Y->X', (7, 8)]

test()

# what problem with X,Y, and goal < 10, has the longest solution?

def num_actions(triplet):
    X,Y,goal = triplet
    return len(fillbucket(X,Y,goal,state = (0,0)))

def hardest(triplet):
    X,Y,goal = triplet
    return num_actions(triplet)-max(X,Y,goal)


print max([(X,Y,goal) for X in range(1,10) for Y in range(1,10) for goal in range (1, max(X,Y))], key = num_actions)


