# decorator
'''A decorator is just a callable that takes a function
as an argument and returns a replacement function.

The @ symbol applies a decorator to a function

*args and **kwargs
We have written a useful decorator but it is hard coded to work only on a particular kind of function -
one which takes two arguments.
Our inner function checker accepts two arguments and passes the arguments on to the function captured
in the closure. What if we wanted a decorator that did something for any possible function?
write a decorator that increments a counter for every function call of every decorated function without changing any of it is decorated functions.
This means it would have to accept the calling signature of any of the functions that
it decorates and also call the functions it decorates passing on whatever arguments were passed to it.'''

'''
n_ary(f) f is binary function that takes 2 arguments f(x,y), or f(x) = x
change binary to n-ary for any given function'''

''' n_ary = decorator1(n_ary)
seq = n_ary(seq)'''

from functools import update_wrapper

# the decorator n_ary modifies function f, to return f(x,_f(*arg)
       
def decorator1(decorator2):
    # decorator2 is itself a decoretor on f, it takes input argument of f
    def decorator1_decorator2(f):
        return update_wrapper(decorator2(f),f) 
    update_wrapper(decorator1_decorator2,decorator2)
    #update the inner function with input decorator2
    return decorator1_decorator2

''' Or
def decorator(d):
    return lambda fn: update_wrapper(d(fn),fn)

decorator = decorator(decorator)'''

@decorator1 #apply decorator1 to function n_ary
def n_ary(f):
    def n_ary_f(x,*args):
        return f(x,n_ary_f(*arg))
    # update_wrapper(n_ary_f,f) #update the inner function with f
    return n_ary_f
