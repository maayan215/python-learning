import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd

points = np.array([
  [2, 4],
  [3, 4],
  [3, 0],
  [2, 2],
  [4, 1]
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