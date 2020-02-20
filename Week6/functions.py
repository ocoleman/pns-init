#Owen Coleman
#A function to square numbers.


def f(x):
    ans = x * x
    return ans

print(f(2))


def power(x, y):
    ans = x
    y = y - 1
    while y > 0:
        ans = ans * x
        y = y - 1
    return ans


#print (power(3, 6))