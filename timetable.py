# My timetable program - Mr H
import time

# Calculate current hour
timeNow = time.localtime()
hour = now.tm_hour

# Determine activity
if hour < 8:
    print('sleeping')
elif hour < 17:
    print('working')
elif hour < 22:
    print('relaxing')
else: print('sleeping')
