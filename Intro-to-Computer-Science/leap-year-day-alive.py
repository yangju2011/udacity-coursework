# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel).

''' problem solving process
1) accumulate days from start to end while X? c
2) design a control procedure to keep looping, add days while day1<day2
3) def isDayBefore 
4) def daysBetweenDates
5) after adding days, day 1 --> next day
6) def nextDay
7) def daysInMonths to calculate nextDay
8) def isLeapYear for daysInMonths

'''
'''
Guide to problems
1. do not panic
2. what are the inputs
3. what are the outputs
4. work through some examples by hand (test)
5. simple mechanical solutions
6. develop incrementaly and test as we go !!! Importance of test, assert

'''


#consider leap year later
def isLeapYear(year):
    if year%4==0: # 1900 is not learp year
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else: 
            return True
    return False

#no leap year consideration first
def daysInMonth(year,month): # return the number of days per month
    if month ==1:
        return 31
    if month ==3:
        return 31
    if month ==5:
        return 31 
    if month ==7:
        return 31 
    if month ==8:
        return 31 
    if month ==10:
        return 31 
    if month ==12:
        return 31
    if month ==4:
        return 30    
    if month ==6:
        return 30
    if month ==9:
        return 30
    if month ==11:
        return 30
    if month ==2:
        if isLeapYear(year):
            return 29
        else:
            return 28
    
#assume each month has 30 days first
def nextDay(year,month,day): # for any given day, return the next date, including year, month, day
    if day == daysInMonth(year,month): #late day of the month
        if month == 12: #late day of the year --> next year
            return year+1,1,1
        else:
            return year, month+1,1 #late day of the month --> next month
    else:
        return year,month,day+1

def isDayBefore(year1,month1,day1,year2,month2,day2): #make sure the first date is before second date
    if year1 < year2:
        return True
    if year1 == year2:
        if month1<month2:
            return True
        if month1==month2:
            return day1<day2
    return False

def daysBetweenDates(year1,month1,day1,year2,month2,day2):
    assert not isDayBefore(year2, month2, day2, year1, month1, day1) #assert to make sure it doesnt fail
    days=0
    while isDayBefore(year1,month1,day1,year2,month2,day2):
        year1,month1,day1=nextDay(year1,month1,day1) #define nextDay
        days += 1 #iterate loop
    return days  

# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args) #always test as we go
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test() # test takes no input
