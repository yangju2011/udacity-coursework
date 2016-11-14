'''
conditional probability
'''

from fractions import Fraction
# Fraction(numerator=0, denominator=1)

import itertools
#  product(), Cartesian product, equivalent to a nested for-loop, multiple sets

sex = ['B','G'] # iterable for products

'''
# product() takes at least 2 arguments
print list(itertools.product('a','b'))
# [('a', 'b')]

print list(itertools.product(sex))
# [('B',), ('G',)]

print list(itertools.product(sex,sex))
# [('B', 'B'), ('B', 'G'), ('G', 'B'), ('G', 'G')]
'''

def two_kids(*variable):
    return list(itertools.product(*variable))

# print two_kids(sex,sex)
# [('B', 'B'), ('B', 'G'), ('G', 'B'), ('G', 'G')]

def one_boy(*variable):
    return [k for k in two_kids(*variable) if 'B' in k]

# print one_boy(sex,sex)
# [('B', 'B'), ('B', 'G'), ('G', 'B')]

def two_boy(*variable):
    return [k for k in two_kids(*variable) if k.count('B') == 2]

# print two_boy(sex,sex)
# [('B', 'B')]

def conP(pred,event,*variable):
    def pred(*variable) :
        return [k for k in event(*variable) if predicate(k)]
    return Fraction(len(pred(*variable)),len(event(*variable)))

print conP(two_boy,one_boy,sex,sex)
# 1/3

day = ['M','T','W','R','F','S','s']

def two_kids_anyday(*variable):
    return list(itertools.product(*variable))
    
# print two_kids_anyday(sex,day,sex,day)
# 196 = 2*7*2*7

def any_kid_on_Tuesday(*variable):
    return [k for k in two_kids_anyday(*variable) if 'T' in k]

# print len(any_kid_on_Tuesday(sex,day,sex,day))
# 52

def any_boy_on_Tuesday(*variable):
    '''kids = []
    for k in two_kids_anyday(*variable):
        if k[0] == 'B' and k[1] =='T':
            kids.append(k)
        elif k[2] =='B' and k[3] =='T':
            kids.append(k)
    return kids'''        
    return [k for k in two_kids_anyday(*variable) if (k[0] == 'B' and k[1] =='T') or (k[2] =='B' and k[3] == 'T')]

# need 'B' followed by 'T'

# print len(any_boy_on_Tuesday(sex,day,sex,day))
# 27

def two_boy_pred(*variable):
    return [k for k in any_boy_on_Tuesday(*variable) if k.count('B') == 2]

variable = sex,day,sex,day
print conP(two_boy_pred,any_boy_on_Tuesday,sex,day,sex,day)
# 13/27


