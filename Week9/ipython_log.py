# IPython log file

get_ipython().run_line_magic('', '')
get_ipython().run_line_magic('logstart', '')
import numpy as np
import matplotlib.pyplot as plt
l = np.arange(0.0, 5.0, 1.0)
y1 = l**2
y2 = l**3
plt.plot(l,l, 'b', label="l")
plt.plot(l, y1, 'g', label="squared")
plt.plot(l, y2, 'r', label="cubed")
plt.legend()
plt.title("f(x)=x, g(x)=x2 and h(x)=x3")
plt.xlabel("x")
plt.ylabel("y")
exit()
