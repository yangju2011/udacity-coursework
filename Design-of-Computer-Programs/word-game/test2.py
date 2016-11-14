
import itertools


def anagrams(phrase, shortest=2):
    """Return a set of phrases with words from WORDS that form anagram
    of phrase. Spaces can be anywhere in phrase or anagram. All words 
    have length >= shortest. Phrases in answer must have words in 
    lexicographic order (not all permutations)."""
    # your code here
    # phrase --> a str of letters without space, can repeat
    letters = phrase.replace(' ','') # REMOVE ALL SPACES IN PHRASES
    words = set(['NTH','PIC', 'YO', 'OY', 'ON','THY'])
 # all possible words set made from the letters
    for w in words:
        if len(w)<shortest:
            words.discard(w) # only consider qualified words
    results = set()
    N = len(letters)

    # starting at shortest words, and extend to longers words
    
        

    '''
    THIS ITERATIONH TAKES TOO LONG TIME
    for i in range(1,N):
        combos = list(itertools.combinations(words,i)) # r-length tuples, in sorted order, no repeated elementsm result is a tuple of i elements  
        for result in combos: # each result is a tuple, ('YO', 'THY', 'NTH', 'OY')
            if sorted(letters) == sorted(''.join(result)): # should not repeat 
                results.add(' '.join(result))

    '''
    return results

print anagrams('PYTHONIC')
