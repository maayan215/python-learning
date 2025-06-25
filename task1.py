import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

points = np.array([
  [1, -1],
  [2, -2],
  [3, -3],
  [4, -4],
  [5, -5]
])

x = points[:, 0]
y = points[:, 1]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def line(x):
    return slope * x + intercept

myline = list(map(line, x))

plt.scatter(x, y)
plt.plot(x, myline)
plt.show()