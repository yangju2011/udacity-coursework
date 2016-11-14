minutes = 60*60*60*7
>>> print (minutes)
1512000
>>> print ('number of miniutes in a week is ' + minutes)

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print ('number of miniutes in a week is ' + minutes)
TypeError: cannot concatenate 'str' and 'int' objects

>>> print ('number of miniutes in a week is ', minutes)
('number of miniutes in a week is ', 1512000)

>>> print ('number of miniutes in a week is ' + str(minutes))
number of miniutes in a week is 1512000
# convert int to string

########################
# recursive expression #
########################

# expression -> expression + operator + expression
# expression -> terminal value

# computer speed: 3.5 G Hz, 3.5 billion times per second

# index
string[<expression>]
'udacity'[0]
'udacity'[0:3]

if string is empty, string[0] out of range, yet a[:], a[:-1] and a[0:] print ''

# other index method #
######################
# str.index(str, beg=0 end=len(string))
# str -- This specifies the string to be searched.
# beg -- This is the starting index, by default its 0.
# end -- This is the ending index, by default its equal to the length of the string.'

# find
# <search string>.find(<target string>, <number>)

# Define a procedure, union,
# that takes as inputs two lists.
# It should modify the first input
# list to be the set union of the two
# lists. You may assume the first list
# is a set, that is, it contains no 
# repeated elements.

def union(p1,p2):
    return [p1.append(_) for _ in p2 if _ not in p1]
# same as
'''
    for e in p2:
        if e not in p1:
            p1.append(e)
'''

# ord(one letter string) --> number
# chr(number) --> one letter string, chr() requires its input to be in the list of integers given by range(256), which is
# a list of all the integers from 0 to 255 inclusive.
