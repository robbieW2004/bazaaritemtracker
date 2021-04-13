# pip install matplotlib or no works
import matplotlib.pyplot as plt
# frick i have no idea how matplotlib works but this seems to do the trick
X, Y = [], []
for line in open('data.txt', 'r'):
  values = [float(s) for s in line.split()]
  X.append(values[0])
  Y.append(values[1])
# tellng the plotter to plot
plt.plot(X, Y)
plt.show()