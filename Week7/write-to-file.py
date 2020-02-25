#OWen Coleman
#Write to a file
#Week 7 25-02-20

with open('myfile.txt', 'a') as f:
    print(f.tell())
    f.write("\nHello, from the line!")
    print(f.tell())