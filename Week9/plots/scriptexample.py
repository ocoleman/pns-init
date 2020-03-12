# IPython log file
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(1.0, 100.0, 100)
y1 = x**2
y2 = 2**x
plt.plot(x, y1, 'g.', label="Squared")
plt.plot(x, y2, 'r.', label="Exponential")

plt.legend()
plt.title("Hello, world")
plt.xlabel("Hello, x")
plt.ylabel("Hello, y")
