''' word game, scrabble'''

# find all possible words made from deck that are also in the dictionary

# WORDS = set(filenameread().upper().split()) # return a set of words

def prefixes(word):
    return [word[:i] for i in range(len(word))]
# everything including '', but not word itself

# print prefixes('love')

def readwordlist(filename):
    wordset = set(filenameread().upper().split())
    # prefixset = set(p for word in wordset for p in prefixes(word))
    for w in wordset:
        prefixset = prefixset | set(prefixes(w))
    return wordset, prefixset

def find_words(hand): # len(word) <=7 
    # given a hand of letters in a strig 'AHBDJKZ'
    # a word contains 1 to len(hand) letters
    # itertools.permutations(hand,i) for i in range(1,N+1), permutations returns a list of ['A,'B'] when i == 2, not 'AB'
    # nested loops!!!!!
    results = set()
    for a in hand: # any letter can be the first letter, or the second
        # word = a
        if a in WORDS: results.add(word)
            # wordset.add(word)
        # hand = remove(hand,a)
        for b in remove(hand,a):
            word = a + b
            if word in WORDS: results.add(word)
            for c in remove(hand,word):
                word = a + b + c
                if word in WORDS: results.add(word)
                for d in remove(hand,word):
                    word = a + b + c + d
                    if word in WORDS: results.add(word)
                    for e in remove(hand,word):
                        word = a + b + c + d + e
                        if word in WORDS: results.add(word)
                        for f in remove(hand,word):
                            word = a + b + c + d + e + f
                            if word in WORDS: results.add(word)
                            for g in remove(hand,word):
                                word = a + b + c + d + e + f + g
                                if word in WORDS: results.add(word)
    return results


def remove(string, letter):
    i = string.find(letter) # remove the first apperance
    return string[:i] + '' + string[i+1:] # this does not change the original string


WORDS = set(['ABC','AK','HI'])
hand = 'ABDIK'   
print find_words(hand)


# permutations can be very slow and hard to modify at individual steps
'''
import itertools

wordset = set(['ABC','AK','HI'])
hand = 'ABCHKI'
# as the len(hand) goes higher, takes very long time, evey causing memory Error
mywordset=set()
for i in range(1,len(hand)+1):
    for _ in itertools.permutations(hand,i):
        word = ''.join(_)
        if word in wordset:
            mywordset.add(word)
print mywordset
# set(['AK', 'HI', 'ABC'])
'''

'''
hand = 'ABC'
myword2 = itertools.permutations(hand,2)
print myword2
>>> [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

mywordset = set()
for w in myword2:
    word = ''.join(w)
    mywordset.add(word)

print mywordset
>>>set(['AC', 'AB', 'BA', 'BC', 'CB', 'CA'])
'''
