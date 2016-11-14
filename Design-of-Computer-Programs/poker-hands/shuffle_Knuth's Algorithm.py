# shuffle
import random

# Knuth's Algorithm P

def shuffle(deck): # deck is a list of cards
    n = len(deck)
    for i in range(0,n):
        j = random.randrange(i,n)
        # i also has the opportunity to be swapped to itself
        swap(deck,i,j) #no need to i = i+1
    return deck

def swap(deck,i,j):
    deck[i],deck[j]=deck[j],deck[i]
    
def shuffle_print(n):
    deck =[1,2,3,5,6]
    for i in range(0,n):
        print shuffle(deck)

shuffle_print(100)
