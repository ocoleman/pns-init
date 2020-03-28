#Owen Coleman
#Weekly Task 7
#Write a program that reads in a text file and outputs the number of e's it contains. The program should take the filename from an argument on the command line.

#Imports the sys module
import sys

#Using the sys.argv command to read a command line input given by the user.
#In this case it will be the second arguement given when running the file in a command terminal.
#The arguemnt given, aka the file name, will be opened and read. Using a for loop the variable "ecount" with be incremented for every "e/E" in the text file.
#Finally, ecount will be printed, giving the total e count in the document.
with open(sys.argv[1], 'r') as f:
    ecount = 0
    text = f.read()
    letters = list(text)
    for i in letters:
        if i=='e' or i=='E':
            ecount += 1
    print(ecount)


