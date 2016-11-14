def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

def fast_fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        pre = 0
        post = 1
        i = 1
        while i < n:
            result = pre + post
            pre = post
            post = result
            i = i + 1
        return result
    '''
current = 0
after = 1
for in in range(0,n):
current, after = after, current + after
 (assign together)
 '''

print fast_fibonacci(36)
