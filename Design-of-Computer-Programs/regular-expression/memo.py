# cache is a data structure
# define a decorator and apply the cache to any function
# @ memo

# n_ary, expressive tool

#@decorator
def memo(f): #performace tool
    '''Decorate that caches the return value for each call to f(arg).
    Then when called again with same args, we can just look it up.'''
    cache = {} # key is argument input, value is f(*args)
    def _f(*args):
        try:
            return cache[args] # a particular args
        except KeyError: # not such keyword in
            cache[args] = result = f(*args) # do the computation if not there
            return result
        except TypeError:
            # args is not hashable, unhashable test, list, compute
            # can't hash list because hash is mutable 
            return f(args) 
    return _f # not directly pass *arg to memo, because memo is applied to funtion

#@decorator
def countcalls(f): #debuging tool 
    def _f(*args):
        callcounts[_f] += 1
        return f(*args)
    callcounts[_f] = 0
    return _f

callcounts = {}


'''def disabled(f):
    return f

memo = disabled ''' #type disabled before using @memo will disable memo, stop the debugging process

@countcalls
@memo
def fib(n): return 1 if n <= 1 else fib(n-1) + fib(n-2)

print 'with @memo'
print 'n, fib, calls'
for i in range(31):
    print i, fib(i), callcounts[fib]
#  callratio is always 1.618, fibonacci converges to that ratio, also the number of calls
#with or without @memo, speed is largely different, also callcounts is different too

'''
without @memo
n, fib, calls
0 1 1
1 1 2
2 2 5
3 3 10
4 5 19
5 8 34
6 13 59
7 21 100
8 34 167
9 55 276
10 89 453
11 144 740
12 233 1205
13 377 1958
14 610 3177
15 987 5150
16 1597 8343
17 2584 13510
18 4181 21871
19 6765 35400
20 10946 57291
21 17711 92712
22 28657 150025
23 46368 242760
24 75025 392809
25 121393 635594
26 196418 1028429
27 317811 1664050
28 514229 2692507
29 832040 4356586
30 1346269 7049123

with @memo
n, fib, calls
0 1 1
1 1 2
2 2 5
3 3 8
4 5 11
5 8 14
6 13 17
7 21 20
8 34 23
9 55 26
10 89 29
11 144 32
12 233 35
13 377 38
14 610 41
15 987 44
16 1597 47
17 2584 50
18 4181 53
19 6765 56
20 10946 59
21 17711 62
22 28657 65
23 46368 68
24 75025 71
25 121393 74
26 196418 77
27 317811 80
28 514229 83
29 832040 86
30 1346269 89'''
# Teacher returns 59 for n = 30

