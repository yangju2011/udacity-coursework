def boggle_words(bard,minlength=3):
    # record the path like the subway for each step, make sure not to repeat
    # for each step, you will have (state,action) --> state
    # here state is a prefix and sq, action is the path by index location, output state is prefix+board[j]
    results = set()
    N=size(board)

    def extend_path(prefix,path):
        if prefix in WORDS and len(prefix)>=minlenth:
            results.add(prefix)
        if prefix in PREFIXES: # i = path[-1] previous square
            for j in neighbors(path[-1],N):
                if board[j]!=BORDER and j not in path: # make sure not to repeat j in the path
                    extend_path(prefix+board[j],path+[j])


    for (i,L) in enumerate (board):
        if board[i]!=BORDER:
            extend_path(L,[i])
            
    return results


    
