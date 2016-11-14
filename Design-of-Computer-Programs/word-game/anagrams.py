# -----------------
# User Instructions
# 
# This homework deals with anagrams. An anagram is a rearrangement 
# of the letters in a word to form one or more new words. 
#
# Your job is to write a function anagrams(), which takes as input 
# a phrase and an optional argument, shortest, which is an integer 
# that specifies the shortest acceptable word. Your function should
# return a set of all the possible combinations of anagrams. 
#
# Your function should not return every permutation of a multi word
# anagram: only the permutation where the words are in alphabetical
# order. For example, for the input string 'ANAGRAMS' the set that 
# your function returns should include 'AN ARM SAG', but should NOT 
# include 'ARM SAG AN', or 'SAG AN ARM', etc...
'''
import itertools

def anagrams(phrase, shortest=2):
    """Return a set of phrases with words from WORDS that form anagram
    of phrase. Spaces can be anywhere in phrase or anagram. All words 
    have length >= shortest. Phrases in answer must have words in 
    lexicographic order (not all permutations)."""
    # your code here
    # phrase --> a str of letters without space, can repeat
    
    letters = phrase.replace(' ','') # REMOVE ALL SPACES IN PHRASES
    words = find_words(letters) # all possible words set made from the letters IN PHRASES
    
    # all possible words set made from the letters
 
   for w in words:
        if len(w)<shortest:
            words.discard(w) # only consider qualified words
    results = set()
    N = len(letters)
    
    for i in range(1,N):
        combos = list(itertools.combinations(words,i)) # r-length tuples, in sorted order, no repeated elementsm result is a tuple of i elements  
        for result in combos: # each result is a tuple, ('YO', 'THY', 'NTH', 'OY')
            if sorted(letters) == sorted(''.join(result)):
                results.add(' '.join(result))

    return results'''
    # iteration works but takes too long time

def anagrams(phrase, shortest=2):
    """Return a set of phrases with words from WORDS that form anagram
    of phrase. Spaces can be anywhere in phrase or anagram. All words 
    have length >= shortest. Phrases in answer must have words in 
    lexicographic order (not all permutations)."""
    # if possible, use recursive finding words
    return helper_anagrams(phrase.replace(' ',''),'',shortest)

def helper_anagrams(letters,previous_word,shortest):
    # results is a tuple of words
    results = set()
    for w in find_words(letters): #for all possible words
        if len(w)>=shortest and w > previous_word: #previous word start from, w1>w1, means in alphabetical order only
            remainder = removed(letters,w)
            if remainder:
                for rest in helper_anagrams(remainder,w,shortest):
                    results.add(w + ' '+rest) # final word from reminders and w>pre_word, and add to the previous words and and rest? 
            else:
                results.add(w) # if there is no remainder, means at the end of the letters
    return results
    
    
def removed(letters, remove):
    "Return a str of letters, but with each letter in remove removed once."
    for L in remove:
        letters = letters.replace(L, '', 1)
    return letters

def find_words(letters): #only find words from letters, but not necessarily use up the phrase
    return extend_prefix('', letters, set())

def extend_prefix(pre, letters, results):
    if pre in WORDS: results.add(pre)
    if pre in PREFIXES:
        for L in letters:
            extend_prefix(pre+L, letters.replace(L, '', 1), results)
    return results

def prefixes(word):
    "A list of the initial sequences of a word, not including the complete word."
    return [word[:i] for i in range(len(word))]

def readwordlist(filename):
    "Return a pair of sets: all the words in a file, and all the prefixes. (Uppercased.)"
    wordset = set(open(filename).read().upper().split())
    prefixset = set(p for word in wordset for p in prefixes(word))
    return wordset, prefixset

WORDS, PREFIXES = readwordlist('words4k.txt')

# ------------
# Testing
# 
# Run the function test() to see if your function behaves as expected.

def test():
    assert 'DOCTOR WHO' in anagrams('TORCHWOOD')
    assert 'BOOK SEC TRY' in anagrams('OCTOBER SKY')
    assert 'SEE THEY' in anagrams('THE EYES')
    assert 'LIVES' in anagrams('ELVIS')
    assert anagrams('PYTHONIC') == set([
        'NTH PIC YO', 'NTH OY PIC', 'ON PIC THY', 'NO PIC THY', 'COY IN PHT',
        'ICY NO PHT', 'ICY ON PHT', 'ICY NTH OP', 'COP IN THY', 'HYP ON TIC',
        'CON PI THY', 'HYP NO TIC', 'COY NTH PI', 'CON HYP IT', 'COT HYP IN',
        'CON HYP TI'])
    return 'tests pass'

print test()

