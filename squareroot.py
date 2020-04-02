#Owen Coleman
#Weekly Task 6
#Write a program that takes a positive floating-point number as input and outputs an approximation of its square root. You should create a function called sqrt that does this.

#Assigns the variable num as the absolute floating point version of the number given by the user. 
# For example, if the number given is -11, the value stored in num will be 11.0
num = abs(float(input("Please enter a positive number: ")))

#Creates a function sqrt which takes in the number num.
def sqrt(num):
    a = num # a is assigned the inital value of num. 
    for i in range(500): # A for loop is created which will run 500 times
        num = 0.5 * (num + a / num) #With each iteration of the for loop the num variable is updated with a closer approximation
                                    #of the its square root. 
    return round(num, 1) #Finally the approxiamtion of the square root is returned, rounded to the nearest decimal place.


print("The square root of", num, "is approx.", sqrt(num)) #Calls the function and prints the result. 