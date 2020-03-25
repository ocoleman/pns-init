#Owen Coleman
#Weekly task 4
#Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. 
#At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. 
# Have the program end if the current value is one.

#Assigns variable v as the entered user input.
v = int(input("Please enter a positive integer:"))


#While the value of v is greater than 1.
while v > 1: 
    #If v is divided by 2 with no remainder, it is equal.
    if v % 2 == 0:
        #Therefore divde v by 2.
        v = v / 2
    else:
        #Otherwise v must be positive, so multiply v by 3 and add 1.
        v = (v * 3) + 1
    #print the current output and repeat (if necessary).
    print(int (v)) 