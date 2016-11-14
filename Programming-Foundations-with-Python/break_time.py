import webbrowser
import time

print "This program started on " + time.ctime() # Wed Aug 10 10:56:50 2016, current time
print time.clock() # 1.60361827599e-06

print webbrowser.get()
# Return a controller object for the browser type name. If name is empty, return a controller for a default browser appropriate to the caller s environment.

break_count = 0
breaktime = 3
while break_count < breaktime:
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=5GL9JoH4Sws",1)
    break_count = break_count+1

    
