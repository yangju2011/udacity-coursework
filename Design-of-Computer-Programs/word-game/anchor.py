# anchor is set, row is list
class anchor(set):
    " An anchor is where a new workd can be replaced; has a set of allowable letter. "
# class has a content body, which here is empty

LETTERS = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

ANY = anchor(LETTERS) # an anchor can be any letter

mnx = anchor('MNX')
moab = anchor('MOAB')

a_row = row  = ['|','A',mnx,moab,'.','.',ANY,'B','E',ANY,'C',ANY,'.',ANY,'D',ANY,'|']
# anchor is represented as a set of any letter
a_hand = 'ABCEHKN'


# already 
def row_plays(hand, row):
    # given a row and hand, return a set of words
    results = set() # in a tuple (i,word), index box and the word it forms

    # to each allowable prefix, add all suffies, keeping words
    
    for (i,sq) in enumerate(row[1:-1],1): # return index and value
        # the value is ANY if it is anchor class. sq is square
        # only consider without borders, but to avoid getting error for borders for indexing
        if isinstance(sq,anchor):
            pre,maxsize = legal_prefix(i)
            if pre: # means the anchor is next to a letter, the letter has then be involved in the word
                start = i - len(pre) # which is also maxsize
                add_suffixes(hand, pre,start, row, results, anchored= False)
            else: # pre = '', means the next is an empty square, up until the next anchor 
                for pre in find_prefixes(hand): # only check allowable prefix made of hande
                    if len(pre) <= maxsize:
                        start = i - len(pre)
                        add_suffixes(hand, pre, start, row, results, anchored= False)   
    return results
    # (i,word)
    # (12,'BEN')
    

def legal_prefix(i,row): # for any anchor at index i, result a set of legal prefix in set (), do not have to be in hand, just check the square it can add 
    # given the position i in row, give all possible prefixes in (character on the very left , maximal length)
    s = i
    while is_letter(row[s-1]): s = s - 1
    if s < i: # there is a prefix, not ''
        return ''.join(row[s:i]), i-s # row [s:i] is a list, not a string
        
    while is_empty(row[s-1]) and not isinstance(row[i-1],anchor): s = s-1 
    return ('',i-s)

def is_letter(sq): # define whether a is a letter "string", not empty, not anchor
    return isinstance(sq,str) and sq in LETTERS # make sure the anchored point is allowable letter 

def is_empty(sq):
    return sq == ',' or sq == '*' or isinstance(sq,anchor)
    # starting location *

def add_suffixes(hand, pre, start, row, results, anchored = False): # not anchored yet
    'add all possible suffiexs, and accumulate (start,word) pairs in result'
    i = start + len(pre) # anchored letter position 
    if pre in WORDS and anchored and not is_letter(row[i]): # at least anchored prefix, not with existing letter 
        results.add((start,pre)) # not 'BE' but 'BE+D'
    if pre in PREFIXES:
        sq = row[i]
        is is_letter(sq): add_suffixes(hand, pre+sq, start, row, results) # if it is a letter, have to be added to prefix, have to use it
        elif is_empty(sq):
            possibilities = sq if isinstance(sq,anchor) else ANY # if a square is an empty, it could also be an anchor, or ',' which is ANY
            for L in hand:
                if L in possibilities:
                    add_suffixes(hand.replace(L,'',1), pre+L, start, row, results)
    return results
                                 
def prefixes(word):
    return [word[:i] for i in range(0,len(word))]

wordset = set(['a','b','cd','efg'])
prefixset = set( [p for w in wordset for p in prefixes(w)])
print prefixset
    

# to make it compact
def find_words(letters, pre='',results=None):
    # add 2 optional arguments 
    if results == None: results = set()
    if pre in wordset: results.add(pre)
    if pre in prefixset: # return the sum of all for loop, if return in the loop, does not loop through 
        for L in letters:
            find_words(letters.replace(L,'',1), pre+L, results)
            # pre has to be in prefix to become a word later 
    return results 
    
def remove(L,string):
    return string.replace(L,'',1) #string is not changed


print find_words('abc')
