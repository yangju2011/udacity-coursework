# ---------------
# User Instructions
#
# Write a function, findtags(text), that takes a string of text
# as input and returns a list of all the html start tags in the 
# text. It may be helpful to use regular expressions to solve
# this problem.
'''
Start tags must have the following format:

1.The first character of a start tag must be a "<" (U+003C) character.
2. The next few characters of a start tag must be the element's tag name.
3. If there are to be any attributes in the next step, there must first be one or more space characters.
4. Then, the start tag may have a number of attributes, the syntax for which is described below. Attributes must be separated from each other by one or more space characters.
5. After the attributes, or after the tag name if there are no attributes, there may be one or more space characters. (Some attributes are required to be followed by a space. See the attributes section below.)
6. Then, if the element is one of the void elements, or if the element is a foreign element, then there may be a single "/" (U+002F) character. This character has no effect on void elements, but on foreign elements it marks the start tag as self-closing.
7. Finally, start tags must be closed by a ">" (U+003E) character.

'''

import re

# <( "[^"]*" | '[^']*' | [^'">] )*>

def findtags(text):
    pattern ='<\s*\w+\s*' + '(?:\s*\w+\s*=\s*"[^"]*"\w*\s*)*' + '\s*/?>'
    return re.findall(pattern,text)

testtext1 = """
My favorite website in the world is probably 
<a href="www.udacity.com">Udacity</a>. If you want 
that link to open in a <b>new tab</b> by default, you should
write <a href="www.udacity.com"target="_blank">Udacity</a>
instead!
"""

testtext2 = """
Okay, so you passed the first test case. <let's see> how you 
handle this one. Did you know that 2 < 3 should return True? 
So should 3 > 2. But 2 > 3 is always False.
"""

testtext3 = """
It's not common, but we can put a LOT of whitespace into 
our HTML tags. For example, we can make something bold by
doing <         b           > this <   /b    >, Though I 
don't know why you would ever want to.
"""

print findtags(testtext1) 
print findtags(testtext2) 
print findtags(testtext3)

''' if pattern = pattern = r'<.*>'

['<a href="www.udacity.com">Udacity</a>', '<b>new tab</b>', '<a href="www.udacity.com"target="_blank">Udacity</a>']
["<let's see>"]
['<         b           > this <   /b    >']

you don't want backslash as the ending quotes

pattern = r'<.*"[^"]*">' means it must have a string, but it does not have to
['<a href="www.udacity.com">', '<a href="www.udacity.com"target="_blank">']
[]
[]
'''


def test():
    assert findtags(testtext1) == ['<a href="www.udacity.com">', 
                                   '<b>', 
                                   '<a href="www.udacity.com"target="_blank">']
    assert findtags(testtext2) == []
    assert findtags(testtext3) == ['<         b           >']
    return 'tests pass'

print test()

