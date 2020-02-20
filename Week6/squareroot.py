# Owen Coleman
#Weekly Task 6
#Write a program that takes a positive floating-point number as input and outputs an approximation of its square root. You should create a function called sqrt that does this.

import math

num = abs(float(input("Please enter a positive number: ")))

def sqrt(num):
   return round(math.sqrt(num), 1)


print("The square root of", num, "is approx.", sqrt(num))