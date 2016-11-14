def mymax(iterable, key = None):
    # key is a function they can take input, None is the value of the function key
    maxval = None
    # any number is bigger than None
    
    xval = key or (lambda x: x)
    # xval is self , xval is a function, which returns x for input x

    for x in iterable:
        if xval(x) > maxval:
            maxval = xval(x)
    return maxval
    

s = [1,2,3]

def minus(x):
    return -x

print mymax(s,key=minus)
