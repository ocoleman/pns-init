#Owen Coleman
#Weekly task 5
#Write a program that outputs whether or not today is a weekday.
#Sourced from w3schools.

#Imports the datetime library from python.
import datetime

#Assigns now as a variable which contains information on the current date and time in the format: YYYY-MM-DD 00:00:00.00000.
now = datetime.datetime.now()

#Using the weekday method will return the numeric value for the current day of the week. With Monday being 0 and Sunday being 6.
#If the value of the current day is less than or equal to 4(Friday), the print 
if now.weekday() <= 4:
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")

