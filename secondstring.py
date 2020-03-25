#Owen Coleman
#Weekly task 3
#Write a program that takes asks a user to input a string and outputs every second letter in reverse order.

#Variable x, the value of the input requested from the user. 
x = input("please enter a sentence:")

#Prints the string, from start to finish, but at a step of -2.
# This will return every second value in reverse order. 
print(x[::-2])