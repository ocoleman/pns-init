#Owen Coleman
#Weekly Task 8
#Write a program that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.

#Imports the numpy and matplotlib libraries.
import numpy as np
import matplotlib.pyplot as plt

#the variable l is assigned generated, evenly spaced values in the range of 0 to 5, exluding 5. The values in this range increment in steps of 1. y1 and y2 sqaure and cube these values repectively.
l = np.arange(0.0, 5.0, 1.0)
y1 = l**2 #squared
y2 = l**3 #cubed

#using matplotlib.pyplot(plt).plot the values generated above are plotted against l, on a single graph.
plt.plot(l,l, 'b', label="l")
plt.plot(l, y1, 'g', label="squared")
plt.plot(l, y2, 'r', label="cubed")

#The following generates a legend, including labels for the x and y axis aswell as a title.
plt.legend()
plt.title("f(x)=x, g(x)=x2 and h(x)=x3")
plt.xlabel("x")
plt.ylabel("y")

#finally the figure is saved as the png file "plot.png". plt.clf() clears the current figure.
plt.savefig("plot.png")
plt.clf()