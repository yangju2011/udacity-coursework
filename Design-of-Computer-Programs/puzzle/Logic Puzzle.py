"""
UNIT 2: Logic Puzzle

You will write code to solve the following logic puzzle:

1. The person who arrived on Wednesday bought the laptop.

2. The programmer is not Wilkes.

3. Of the programmer and the person who bought the droid,
   one is Wilkes and the other is Hamming.
   
4. The writer is not Minsky.

5. Neither Knuth nor the person who bought the tablet is the manager.

6. Knuth arrived the day after Simon.
7. The person who arrived on Thursday is not the designer.

8. The person who arrived on Friday didn't buy the tablet.
9. The designer didn't buy the droid.
10. Knuth arrived the day after the manager.

11. Of the person who bought the laptop and Wilkes,
    one arrived on Monday and the other is the writer.
12. Either the person who bought the iphone or the person who bought the tablet
    arrived on Tuesday.

You will write the function logic_puzzle(), which should return a list of the
names of the people in the order in which they arrive. For example, if they
happen to arrive in alphabetical order, Hamming on Monday, Knuth on Tuesday, etc.,
then you would return:

['Hamming', 'Knuth', 'Minsky', 'Simon', 'Wilkes']

(You can assume that the days mentioned are all in the same week.)
"""

import itertools

def logic_puzzle():
    "Return a list of the names of the people, in the order they arrive."
    ## your code here; you are free to define additional functions if needed
    days = [Monday, Tuesday, Wednesday, Thursday, Friday] = [1,2,3,4,5]
    orderings = list(itertools.permutations(days)) # the ordering needs to be an explict list
 
    # generator next(p for p in xx)
    
    answer = next([Hamming, Minsky, Simon, Knuth, Wilkes]
                for [Hamming, Minsky, Simon, Knuth,Wilkes] in orderings
                if Knuth == Simon + 1 #6
            
                for [programer, writer, designer, manager, _] in orderings
                if writer != Minsky #4
                if designer != Thursday #7
                if Knuth == manager + 1 #10
                if programer != Wilkes #2
            
                for [iphone, tablet, droid, laptop, _] in orderings
                
                if Wednesday == laptop #1
                if (tablet != manager and Knuth != manager)#5
                if Friday != tablet #8
                if designer != droid #9
                if (iphone == Tuesday or tablet == Tuesday) #12
                if set([programer, droid]) == set([Wilkes, Hamming]) #3 # set expected at most 1 arguments got 2            
                if set([laptop, Wilkes]) == set([Monday, writer]) #11
                )

    # return it in the correct sorted number'
    [Hamming, Minsky, Simon, Knuth, Wilkes] = answer
    names = {Hamming:'Hamming', Minsky:'Minsky', Simon:'Simon', Knuth:'Knuth', Wilkes:'Wilkes'}
    sortn = sorted(answer)
    return [names[k] for k in sortn]

        
print logic_puzzle()
                
                
                
                
    
