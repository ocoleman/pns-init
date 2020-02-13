#Owen Coleman
#Computing the primes.


# My list of primes

P = []

# Loop through all the numbers we're checking for primality.
for i in range(2, 100):
    isprime = True
    # Loop through all vlaies from2 up to but not including i.
    for j in range(2, i):
        if i % j == 0:
            # If it does, i isn't prime so exit the loop and indicate it's not prime.
            isprime = False
            break
    if isprime:
        P.append(i)

print(P)