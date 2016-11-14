# regular expression
# find pattern in text
'''
special pattern sign
. any character
? one or no character before ? ab? --> a or ab
* multiple character ab* -->a,ab,abbbbb
^ start with character ^ab --> start with ab
$ end with character ab$ --> end with ab
'''

def search(pattern,text):
    "exist anythere in the text"
    if pattern.startswith('^'):
        return match(pattern[1:],text) #remember to return
    else:
        return match('.*'+pattern,text)
    
def match(pattern,text):
    "exist at the beginning of the text"
    if pattern == '':
        return True
    elif pattern == '$':
        return (text == '')
    elif len(pattern)>1 and pattern[1] in '?*': # in, not ==
        p = pattern[0]
        op = pattern[1]
        rp = pattern[2:] # if len(pattern) = 2, rp = ''
        if op == '?':
            return match(rp,text) or (matchfirst(p,text) and match(rp,text[1:]))
        # no p
        # if p, then matchfirst p and match rest pattern to text[1:]
        # here only the first char is matched, so the rest of the text is text[1:] not text[2:]
        else: #if op == '*'
            return matchstar(p,rp,text)
    else:
        return (matchfirst(pattern[0],text) and match(pattern[1:],text[1:]))

def matchfirst(p,text):
    # p is an element of pattern, a character
    if not text: #text is empty ''
        return False
    else: 
        if p == '.': # also if p == '.', would work anyway
            return True
        else:
            return p == text[0]
        #text[0] is error if text == ''
    

    
    # pattern= a*b, text = aaaaab
    # text[1:] = 'b'
    # then matchfirst is False, 
    # p = a, rp = b
    # p is a character, rp is a pattern
    # uncertain number (>=2 )of p followed by rp to match a text, p is always at start
def matchstar(p,rp,text):
    return match(rp,text) or (matchfirst(p,text) and matchstar(p,rp,text[1:]))
    # if rp matches text, means there is no p
    # or one p or more p
    # match first, then check others

def test():
    text = 'baa!'
    p1 = 'a!'
    p2 = ''
    p3 = '$'
    p4 = 'a?'
    p5 = 'a*'
    p6 = 'a.'
    p7 = 'ba.'
    p8 = 'c'
    assert search(p1,text) == True
    assert search(p2,text) == True
    assert search(p3,text) == True # search $ means '' before $
    assert search(p4,text) == True
    assert search(p5,text) == True
    assert search(p6,text) == True
    assert search(p7,text) == True
    assert search(p8,text) == False
    
    assert match(p1,text) == False
    assert match(p2,text) == True
    assert match(p3,text) == False
    assert match(p4,text) == True # a or ''
    assert match(p5,text) == True
    assert match(p6,text) == False
    assert match(p7,text) == True
    assert match(p8,text) == False
    return 'test passed'

print test()
    
