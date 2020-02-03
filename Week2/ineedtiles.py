# This program calculates hoe many tiles you will need
# when tiling a wall or floor (in m2).

length = float(input("enter room length: "))
width = float(input("enter room width: "))


# length = 2.0
# width = 2.0

area = length * width

needed = area * 1.05

print("You need", needed, "tiles in metres squared.")