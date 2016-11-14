# Write a procedure, shift_n_letters which takes as its input a lowercase
# letter, a-z, and an integer n, and returns the letter n steps in the
# alphabet after it. Note that 'a' follows 'z', and that n can be positive,
#negative or zero.

def shift_n_letters(letter, n):
    minlimit=ord('a')
    maxlimit=ord('z')
    if ord(letter)+n >= minlimit and ord(letter)+n <=maxlimit:
        return chr(ord(letter)+n)
    else:
        if ord(letter)+n >maxlimit:
            return chr(minlimit+ord(letter)+n - maxlimit-1)
        if ord(letter)+n<minlimit:
            return chr(maxlimit-(minlimit-(ord(letter)+n))+1)

print shift_n_letters('a', -1)
#>>> t
print shift_n_letters('s', 2)
#>>> u
print shift_n_letters('s', 10)
#>>> c
print shift_n_letters('z', 1)
#>>> i
