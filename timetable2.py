# My timetable program - Mr H
import time
def get_time()
    global hourNow
    hourNow = now.tm_hour
#main program
get_time()
if hourNow >= 9 and hourNow <= 15:
    msg = 'school'
elif hourNow > 15 and hourNow < 18:
    msg = 'homework'
elif hourNow >= 18 and hourNow < 22:
    msg = 'relaxing'
else: msg = 'sleeping'
print(msg)
