a = ['abcd','bcde','cdef']
word = 'mn'
row = a[1]
j = 1
newrow = row[:j]+word+row[j+len(word):]
a[1] = newrow
print a
# ['abcd', 'bmne', 'cdef']
