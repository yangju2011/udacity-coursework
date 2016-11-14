# -----------------
# User Instructions
# 
# Write a function, subway, that takes lines as input (read more about
# the **lines notation in the instructor comments box below) and returns
# a dictionary of the form {station:{neighbor:line, ...}, ... } 
#
# For example, when calling subway(boston), one of the entries in the 
# resulting dictionary should be 'foresthills': {'backbay': 'orange'}. 
# This means that foresthills only has one neighbor ('backbay') and 
# that neighbor is on the orange line. Other stations have more neighbors:
# 'state', for example, has 4 neighbors.
#
# Once you've defined your subway function, you can define a ride and 
# longest_ride function. ride(here, there, system) takes as input 
# a starting station (here), a destination station (there), and a subway
# system and returns the shortest path.
#
# longest_ride(system) returns the longest possible ride in a given 
# subway system. 

# -------------
# Grading Notes
#
# The subway() function will not be tested directly, only ride() and 
# longest_ride() will be explicitly tested. If your code passes the 
# assert statements in test_ride(), it should be marked correct.


def subway(**lines):
    stations = {}
    neighbors = {}
    
    for e in lines:
        station_e = lines[e].split()
        n = len(station_e)
        for i,s in enumerate(station_e):
            
            if i == 0:
                neighbor = [station_e[i+1]]
            if i == n-1:
                neighbor = [station_e[i-1]]
            else:
                neighbor = [station_e[i-1],station_e[i+1]]

            if s in neighbors:
                neighbors[s] = neighbors[s] + neighbor
            else:
                neighbors[s] = neighbor # neighbor is already a list
               
            if s not in stations:
                stations[s]= [e]
            else:
                stations[s].append(e)

    outs = {}
    for s in stations:
        values = {}
        neighbor = neighbors[s] # a list of neighbors
        for n in neighbor: # n is a string, the line is on both s and n
            line_n = stations[n]
            line_s = stations[s]
            values[n]=[]
            for l in line_n:
                if l in line_s:
                    if l not in values:
                        values[n].append(l)
                    # if values[n]: # values[n] is not defined yet
                    # here make sure each n is unique, there could be multiple l  that satifiy the if statement
        outs[s]= values
    return outs


new_york = subway(
    line_1 = 'a,b,c'
    line_2 = ''
    line_3
    line_4
    line_5
    line_6
    line_7
    line_A
    line_B
    line_C
    line_D
    line_E
    line_F
    line_G
    line_J
    line_L
    line_M
    line_N
    line_Q
    line_R
    line_S = '')


def ride(here, there, system=boston):

    start = here
    if start == there:
        return [start]
    
    def is_goal(state):
        return state == there

    def successors(state):
        outs2 = {}
        nls = system[state] # {n:[l],n:l}
        for e in nls:
            ls = nls[e]
            for l in ls:
                outs2[e] = l
        return outs2
    
        # which is already neighbor:[action] (line)                
    
    return shortest_path_search(start, successors, is_goal)

def longest_ride(system):

    all_paths= [(ride(here, there, system=boston)) for here in system for there in system]
    return max(all_paths,key=len)

def shortest_path_search(start, successors, is_goal):

    if is_goal(start):
        return [start]
    explored = set(start) # set of states we have visited
    frontier = [ [start] ] # ordered list of paths we have blazed
    while frontier:
        path = frontier.pop(0)
        s = path[-1]
        for (state, action) in successors(s).items():
            if state not in explored:
                explored.add(state)
                path2 = path + [action, state]
                if is_goal(state):
                    return path2
                else:
                    frontier.append(path2)

    return []

def path_states(path):
    return path[0::2]
    
def path_actions(path):
    return path[1::2]

