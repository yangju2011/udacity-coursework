def is_letter(a):
    return a!= '.' and a!='|' and not isinstance(a,set)

class anchor(set):
    " anchor is just another set"

letters = list('abcdefg')
ANY = anchor(letters)

print is_letter('a')
