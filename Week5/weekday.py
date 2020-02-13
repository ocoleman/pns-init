#Owen Coleman
#A program that outputs whether or not today is a weekday.

import datetime

now = datetime.datetime.now()



if now.weekday() <= 4:
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")

