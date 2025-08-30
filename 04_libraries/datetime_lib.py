"""
datetime library is used in managing date and time in python. lets see its different functions.
"""

import datetime

#   get current date and time in format: yyyy-mm-dd hh:mm:ss.sss in 24 hour format.
print(datetime.datetime.now())

#   get date and time, time stamp value
print(datetime.datetime.now().timestamp())

#   get current date
print(datetime.datetime.today())

#   get the day number. 1 for monday, 2 for tuesday and so on.
print(datetime.datetime.now().isoweekday())

