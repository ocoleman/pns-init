# IPython log file

get_ipython().run_line_magic('logstart', '')
import pandas as pd
pd.read_csv("http://www.biostat.jhsph.edu/~rpeng/useRbook/faithful.csv")
df = pd.read_csv("http://www.biostat.jhsph.edu/~rpeng/useRbook/faithful.csv")
df
df["waiting"]
import matplotlib.pyplot as plt
plt.plot(df["eruptions"], df["waiting"], 'b.')
plt.hist(df["eruptions"])
plt.savefig("hist.png")
plt.hist(df["eruptions"])
plt.savefig("hist.png")
exit()
