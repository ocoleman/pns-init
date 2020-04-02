#Owen Coleman
#Weekly Task 6
#Write a program that takes a positive floating-point number as input and outputs an approximation of its square root. You should create a function called sqrt that does this.

#Imports the python math library
import math

#Assigns the variable num as the absolute floating point version of the number given by the user. 
# For example, if the number given is -11, the value stored in num will be 11.0
num = abs(float(input("Please enter a positive number: ")))

def sqrt(num):
   return round(num**(1/2), 1)


print("The square root of", num, "is approx.", sqrt(num))