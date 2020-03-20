import sys
import myfunctions

#Get n from the command line.
n = int(sys.argv[1])
# Caclucate factorial of n.
ans = myfunctions.factorial(n)
#print answer.
print("the factorial of ", n, "is:", ans)
