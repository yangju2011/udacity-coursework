# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.

def shift_n_letters(letter, n):
    minlimit=ord('a')
    maxlimit=ord('z')
    if ord(letter)+n >= minlimit and ord(letter)+n <=maxlimit:
        return chr(ord(letter)+n)
    else:
        if ord(letter)+n >maxlimit:
            return chr(minlimit+ord(letter)+n - maxlimit-1) #check boundry a-z,z-a
        if ord(letter)+n<minlimit:
            return chr(maxlimit-(minlimit-(ord(letter)+n))+1)

def rotate(word,n):
    # Your code here
    '''newword=''
    for letter in word:
        if letter !=' ': #if not space
            newletter=shift_n_letters(letter, n)
        else:
            newletter=' ' # do not shift space
        newword=newword+newletter
    return newword'''
    return ''.join([shift_n_letters(letter,n) for letter in word if letter !=' ']) # ([]) is ['a','b','c'], ''.join([]) --> create a string
    # this does not make ' ' to ' '

print rotate ('sarah', 13)
#>>> 'fnenu'
print rotate('fnenu',13)
#>>> 'sarah'
print rotate('dave',5)
#>>>'ifaj'
print rotate('ifaj',-5)
#>>>'dave'
print rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17)
#>>> if your code works correctly you should be able to read this
