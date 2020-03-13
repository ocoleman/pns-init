#Owen Coleman

v = int(input("Please enter a positive integer:"))

while v > 1:
    print(int (v))
    if v % 2 == 0:
        v = v / 2
    else:
        v = (v * 3) + 1
        