# ---------------
# User Instructions
#
# Modify the function, trace, so that when it is used
# as a decorator it gives a trace as shown in the previous
# video. You can test your function by applying the decorator
# to the provided fibonnaci function.
#
# Note: Running this in the browser's IDE will not display
# the indentations.

# trace is a tool

from functools import update_wrapper


def decorator(d):
    "Make function d a decorator: d wraps a function fn."
    def _d(fn):
        return update_wrapper(d(fn), fn)
    update_wrapper(_d, d)
    return _d

@decorator
def trace(f):
    indent = '   '
    def _f(*args):
        signature = '%s(%s)' % (f.__name__, ', '.join(map(repr, args)))
        #function name, f(*args), and repetitive inputs
        print '%s--> %s' % (trace.level*indent, signature)
        trace.level += 1
        try:
            # your code here
            result = f(*args) # arg input is unknowmn, thus for any arg
            print '%s<-- %s == %s' % ((trace.level-1)*indent, 
                                      signature, result)
        finally:
            trace.level -= 1 #decrease by 1 level
            # your code here
        return result #compute result in the decorator and return it
    trace.level = 0
    return _f

@trace
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

fib(6) #running this in the browser's IDE  will not display the indentations!
'''
--> fib(6)
   --> fib(5)
      --> fib(4)
         --> fib(3)
            --> fib(2)
               --> fib(1)
               <-- fib(1) == 1
               --> fib(0)
               <-- fib(0) == 1
            <-- fib(2) == 2
            --> fib(1)
            <-- fib(1) == 1
         <-- fib(3) == 3
         --> fib(2)
            --> fib(1)
            <-- fib(1) == 1
            --> fib(0)
            <-- fib(0) == 1
         <-- fib(2) == 2
      <-- fib(4) == 5
      --> fib(3)
         --> fib(2)
            --> fib(1)
            <-- fib(1) == 1
            --> fib(0)
            <-- fib(0) == 1
         <-- fib(2) == 2
         --> fib(1)
         <-- fib(1) == 1
      <-- fib(3) == 3
   <-- fib(5) == 8
   --> fib(4)
      --> fib(3)
         --> fib(2)
            --> fib(1)
            <-- fib(1) == 1
            --> fib(0)
            <-- fib(0) == 1
         <-- fib(2) == 2
         --> fib(1)
         <-- fib(1) == 1
      <-- fib(3) == 3
      --> fib(2)
         --> fib(1)
         <-- fib(1) == 1
         --> fib(0)
         <-- fib(0) == 1
      <-- fib(2) == 2
   <-- fib(4) == 5
<-- fib(6) == 13
'''
