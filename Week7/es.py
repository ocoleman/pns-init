#Owen Coleman
#Weekly Task 7
import sys

with open(sys.argv[1], 'r') as f:
    ecount = 0
    text = f.read()
    letters = list(text)
    for i in letters:
        if i=='e' or i=='E':
            ecount += 1
    print(ecount)


