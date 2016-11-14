# timecall

def timecall(fn,*arg):
    t0 = time.clock()
    result=fn(*arg)
    t1 = time.clock()
    return t1-t0,result

def average(numbers):
    "Return the average (arithmetic mean) of a sequence of numbers."
    return sum(numbers) / float(len(numbers)) 

def timedcalls(n, fn, *args):
    """Call fn(*args) repeatedly: n times if n is an int, or up to
    n seconds if n is a float; return the min, avg, and max time"""
    # Your code here.
    if isinstance(n,int):
        times = [timecall(fn,*args)[0] for x in range(n)]
    else:
        # up tp n seconds, meaning the time.clock() == n
        times = []
        while sum(times) < n: #sum of the times, up to seconds, sum of all single time in second in []
            times.append(timecall(fn,*args)[0])
    return min(times), average(times), max(times)
