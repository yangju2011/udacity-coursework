import time

def time_execution(code):
    start = time.clock() # start the clock, time now
    result = eval (code) # evaluate the code, or run the code
    run_time = time.clock() - start
    print result, run_time

time_execution('2**10')
time_execution('1+1')
# eval + string code
# (1024, 5.580521798031294e-05), just 1.5x slower than 1+1
# (2, 3.8165637584242074e-05) 0.0000381 s *10^6 = 38us

# The actual processing time is even lower, because, for instance, starting and stopping the clock.

time_execution('time.clock()')


# spin loop runtime

def spin_loop(n):
    i = 0
    while i < n:
        i = i + 1


time_execution('spin_loop(10**2)')
time_execution('spin_loop(10**3)')
time_execution('spin_loop(10**4)')
time_execution('spin_loop(10**8)')

# runtime increases as input size goes up
