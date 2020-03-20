#Owen Coleman

import sys


try:

    with open (sys.argv[1]) as f:
        print(f.read())
    a = 1 / 0
except FileNotFoundError:
    print("File " + sys.argv[1] + " does not exist.")
except ZeroDivisionError:
    print("This is the division zero error handler.")
except: 
    print("All other errors.")