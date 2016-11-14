'''def target(filename):
    wordset = set(filename.read().upper().slice())
    prefixset = [p for w in wordset for p in prefixes(w)]
    prefixset = set()
    for w in wordset:
        for p in 
        prefixset.add(p)
    return wordset, prefixset'''

def prefixes(word):
    return [word[:i] for i in range(0,len(word))]

wordset = set(['a','b','cd','efg'])
prefixset = set( [p for w in wordset for p in prefixes(w)])
print prefixset
    

def find_words(letters): # letters is a string of letters called hand
    results = set()

    def extend_prefix(w,letters):
        if w in wordset: return results.add(w)
        if w in prefixset: return
        for L in letters: extend_prefix(w+L,letters.replace(L,'',1))

    extend_prefix('',letters)
    return results


# function 2, 2 separate functions
def find_words_2(letters):
    return extend_prefix('',letters,set())

def extend_prefix(w,letters,results): #not return anything
    if w in wordset: results.add(w)
    if w in prefixset:
        for L in letters:
            extend_prefix(w+L,letters.replace(L,'',1)) #recursice separate 
    return results

# to make it compact
def find_words_3(letters, pre='',results=None):
    # add 2 optional arguments 
    if results == None: results = set()
    if pre in wordset: results.add(pre)
    if pre in prefixset: # return the sum of all for loop, if return in the loop, does not loop through 
        for L in letters:
            find_words_3(letters.replace(L,'',1), pre+L, results)
            # pre has to be in prefix to become a word later 
    return results 
    
def remove(L,string):
    return string.replace(L,'',1) #string is not changed


print find_words('abc')
