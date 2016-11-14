"""
UNIT 4: Search

Your task is to maneuver a car in a crowded parking lot. This is a kind of 
puzzle, which can be represented with a diagram like this: 

| | | | | | | |  
| G G . . . Y |  
| P . . B . Y | 
| P * * B . Y @ 
| P . . B . . |  
| O . . . A A |  
| O . S S S . |  
| | | | | | | | 

A '|' represents a wall around the parking lot, a '.' represents an empty square,
and a letter or asterisk represents a car.  '@' marks a goal square.
Note that there are long (3 spot) and short (2 spot) cars.

Your task is to get the car that is represented by '**' out of the parking lot
(on to a goal square).  Cars can move only in the direction they are pointing.  
In this diagram, the cars GG, AA, SSS, and ** are pointed right-left,
so they can move any number of squares right or left, as long as they don't
bump into another car or wall.  In this diagram, GG could move 1, 2, or 3 spots
to the right; AA could move 1, 2, or 3 spots to the left, and ** cannot move 
at all. In the up-down direction, BBB can move one up or down, YYY can move 
one down, and PPP and OO cannot move.

You should solve this puzzle (and ones like it) using search.  You will be 
given an initial state like this diagram and a goal location for the ** car;
in this puzzle the goal is the '.' empty spot in the wall on the right side.
You should return a path -- an alternation of states and actions -- that leads
to a state where the car overlaps the goal.

An action is a move by one car in one direction (by any number of spaces).  
For example, here is a successor state where the AA car moves 3 to the left:

| | | | | | | |  
| G G . . . Y |  
| P . . B . Y | 
| P * * B . Y @ 
| P . . B . . |  
| O A A . . . |  
| O . . . . . |  
| | | | | | | | 

And then after BBB moves 2 down and YYY moves 3 down, we can solve the puzzle
by moving ** 4 spaces to the right:

| | | | | | | |
| G G . . . . |
| P . . . . . |
| P . . . . * *
| P . . B . Y |
| O A A B . Y |
| O . . B . Y |
| | | | | | | |

You will write the function

    solve_parking_puzzle(start, N=N)

where 'start' is the initial state of the puzzle and 'N' is the length of a side
of the square that encloses the pieces (including the walls, so N=8 here).

We will represent the grid with integer indexes. Here we see the 
non-wall index numbers (with the goal at index 31):

 |  |  |  |  |  |  |  |
 |  9 10 11 12 13 14  |
 | 17 18 19 20 21 22  |
 | 25 26 27 28 29 30 31
 | 33 34 35 36 37 38  |
 | 41 42 43 44 45 46  |
 | 49 50 51 52 53 54  |
 |  |  |  |  |  |  |  |

The wall in the upper left has index 0 and the one in the lower right has 63.
We represent a state of the problem with one big tuple of (object, locations)
pairs, where each pair is a tuple and the locations are a tuple.  Here is the
initial state for the problem above in this format:
"""

puzzle1 = (
 ('@', (31,)),
 ('*', (26, 27)), 
 ('G', (9, 10)),
 ('Y', (14, 22, 30)), 
 ('P', (17, 25, 33)), 
 ('O', (41, 49)), 
 ('B', (20, 28, 36)), 
 ('A', (45, 46)), 
 ('|', (0, 1, 2, 3, 4, 5, 6, 7, 8, 15, 16, 23, 24, 32, 39,
        40, 47, 48, 55, 56, 57, 58, 59, 60, 61, 62, 63)))
    
# A solution to this puzzle is as follows:

#     path = solve_parking_puzzle(puzzle1, N=8)
#     path_actions(path) == [('A', -3), ('B', 16), ('Y', 24), ('*', 4)]

# That is, move car 'A' 3 spaces left, then 'B' 2 down, then 'Y' 3 down, 
# and finally '*' moves 4 spaces right to the goal.

# Your task is to define solve_parking_puzzle:

N = 8

# But it would also be nice to have a simpler format to describe puzzles,
# and a way to visualize states.
# You will do that by defining the following two functions:

def locs(start, n, incr=1):
    "Return a tuple of n locations, starting at start and incrementing by incr."
    loci = [0]*n
    i = 0
    while i < n:
        loci[i]= start + incr*i
        i = i + 1
    return tuple(loci)

# print locs(26,2)
# print locs(41,2,8)
# print locs(0,8)+ locs(8,2,7)+locs(16,2,7)+locs(24,2,7)+locs(32,2,7)+locs(40,2,7)+locs(48,2,7)+locs(56,8)

def grid(cars, N=N):
    """Return a tuple of (object, locations) pairs -- the format expected for
    this puzzle.  This function includes a wall pair, ('|', (0, ...)) to 
    indicate there are walls all around the NxN grid, except at the goal 
    location, which is the middle of the right-hand wall; there is a goal
    pair, like ('@', (31,)), to indicate this.
    The variable 'cars'  is a tuple of pairs like ('*', (26, 27)).
    The return result is a big tuple of the 'cars' pairs along with the walls and goal pairs."""
    # cars pairs and walls and goal pairs
    goal = ('@', (31,)) # fixed value
    walls_loci = locs(0,8)+ locs(8,2,7)+locs(16,2,7)+locs(24,1,7)+locs(32,2,7)+locs(40,2,7)+locs(48,2,7)+locs(56,8) #wall has less value
    walls = ('|',walls_loci) #fixed value
    return (goal,)+cars+(walls,) # use (goal,) to add tuple, not goal + 
    

puzzle1 = grid((
    ('*', locs(26, 2)),
    ('G', locs(9, 2)),
    ('Y', locs(14, 3, N)),
    ('P', locs(17, 3, N)),
    ('O', locs(41, 2, N)),
    ('B', locs(20, 3, N)),
    ('A', locs(45, 2))))

puzzle2 = grid((
    ('*', locs(26, 2)),
    ('B', locs(20, 3, N)),
    ('P', locs(33, 3)),
    ('O', locs(41, 2, N)),
    ('Y', locs(51, 3))))

puzzle3 = grid((
    ('*', locs(25, 2)),
    ('B', locs(19, 3, N)),
    ('P', locs(36, 3)),
    ('O', locs(45, 2, N)),
    ('Y', locs(49, 3))))

def solve_parking_puzzle(start, N=N):
    """Solve the puzzle described by the starting position (a tuple 
    of (object, locations) pairs).  Return a path of [state, action, ...]
    alternating items; an action is a pair (object, distance_moved),
    such as ('B', 16) to move 'B' two squares down on the N=8 grid."""
    return shortest_path_search(start, psuccessors, is_goal)


puzzle1 = (
 ('@', (31,)),
 ('*', (26, 27)), 
 ('G', (9, 10)),
 ('Y', (14, 22, 30)), 
 ('P', (17, 25, 33)), 
 ('O', (41, 49)), 
 ('B', (20, 28, 36)), 
 ('A', (45, 46)), 
 ('|', (0, 1, 2, 3, 4, 5, 6, 7, 8, 15, 16, 23, 24, 32, 39,
        40, 47, 48, 55, 56, 57, 58, 59, 60, 61, 62, 63)))
'''
      
| | | | | | | |
| G G . . . Y |
| P . . B . Y |
| P * * B . Y @
| P . . B . . |
| O . . . A A |
| O . . . . . |
| | | | | | | | 
| | | | | | | |
| G G . . . . |
| P . . . . . |
| P * * . . . @
| P . . B . Y |
| O A A b . Y |
| O . . b . Y |
| | | | | | | |'''


def psuccessors(state): # state is the whole board represented by grid, return state and actions, which forms path
    # a dictionary
    results = {} # (state, action)
    for c in state:
        if c[0]!='|' and c[0]!='@':
            # c[1] represents car position, 2 or 3 letters
            # if horizontal
            loc = c[1]
            occupied = occupied_loci(state)
            
            if is_hori(loc): # could move right and left
                left,right,length = boundry(loc)
                l = 1
                while (left-l) not in occupied:
                    l = l + 1
                max_dec_step = l-1
                
                if max_dec_step != 0:
                    for i in range(1,max_dec_step+1):
                        newloc = locs(left-i,length) #update c[0] location, update in a tuple
                        action = (c[0],-i)
                        newc = (c[0],newloc)
                        new_state = newstate(state,c,newc)
                        results[new_state] = action
                                
                
                r = 1
                while (right+r) not in occupied:
                    r = r + 1
                max_inc_step = r-1
                
                if max_inc_step != 0:
                    for i in range(1,max_inc_step+1):
                        newloc = locs(left+i,length) #update state # still start with left
                        action = (c[0],i)
                        newc = (c[0],newloc)
                        new_state = newstate(state,c,newc)
                        results[new_state] = action

            else:
                up, down,length = boundry(loc)
                
                l = 1
                while (up - N*l) not in occupied:
                    l = l + 1
                    
                max_dec_step = l-1

                if max_dec_step != 0:
                    for i in range(1,max_dec_step+1):
                        newloc = locs(up-N*i,length,N) #update c[0] location, update in a tuple, both start with up
                        action = (c[0],-N*i)
                        newc = (c[0],newloc)
                        new_state = newstate(state,c,newc)
                        results[new_state] = action
                
                r = 1
                while (down + N*r) not in occupied:
                    r = r + 1
                max_inc_step = r-1

                if max_inc_step != 0:
                    for i in range(1,max_inc_step+1):
                        newloc = locs(up+N*i,length,N) #update state, start with up
                        action = (c[0],N*i) # (B,8) --> NEW LOC = locs(DOWN+8, 3, N)
                        newc = (c[0],newloc)
                        new_state = newstate(state,c,newc)
                        results[new_state] = action          
    return results
    

def newstate(state,c,newc):
    results = []
    for s in state:
        if s != c:
            results.append(s)
        else:
            results.append(newc)
    return tuple(results)            
    
def occupied_loci(state): # @ is not occupied, exit
    results = []
    for c in state:
        if c[0] != '@':
            for l in c[1]:
                results.append(l)
    return sorted(results)

def boundry(loc_tuple):
    return min(loc_tuple), max(loc_tuple),len(loc_tuple)

def is_hori(loc_tuple): #c[1] = loc_tuple
    return (loc_tuple[1]-loc_tuple[0]) == 1

# print psuccessors(puzzle1)

def show(state, N=N):
    "Print a representation of a state as an NxN grid."
    # Initialize and fill in the board.
    board = ['.'] * N**2
    for (c, squares) in state:
        for s in squares:
            board[s] = c
    # Now print it out
    for i,s in enumerate(board):
        print s,
        if i % N == N - 1: print
# show(puzzle1)
# Here we see the grid and locs functions in use:

# Here are the shortest_path_search and path_actions functions from the unit.
# You may use these if you want, but you don't have to.

def shortest_path_search(start, successors, is_goal):
    """Find the shortest path from start state to a state
    such that is_goal(state) is true."""
    if is_goal(start): # start is a tuple board, and path is moved
        return [] # nothing is moved at allm the path is None, return action only 
    explored = set() # set of states we have visited
    frontier = [ [start] ] # ordered list of paths we have blazed, start is not a path though, state to explore 
    while frontier:
        path = frontier.pop(0)
        s = path[-1] # last state
        for (state,action) in successors(s).items(): #The method items() returns a list of dict's (key, value) tuple pairs
            if state not in explored:
                explored.add(state) #state is a large tuple
                path2 = path + [action, state] # path is (action,state) pair, path[-1] is a state
                actions = path_actions(path2)
                if is_goal(state):
                    return actions
                else:
                    frontier.append(path2)
    return []

def is_goal(state):
     for c in state:
         if c[0] == '*':
             return 31 in c[1]

# print is_goal(puzzle1)

def path_actions(path):
    "Return a list of actions in this path."
    return path[1::2]


print solve_parking_puzzle(puzzle1,N=N)
