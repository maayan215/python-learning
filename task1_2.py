import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
points = np.array([
  [2, 4],
  [3, 4],
  [3, 0],
  [2, 2],
  [4, 1]
])

x = points[:, 0]
y = points[:, 1]

correlation_coefficient = pd.DataFrame.corr(pd.DataFrame(points)).loc[1][0]
stdX= np.std(x)
stdY= np.std(y)

slope = (stdY/stdX) * correlation_coefficient

intercept = np.mean(y) - slope * np.mean(x)

def line(x):
    return slope * x + intercept

myline = list(map(line, x))

plt.scatter(x, y)
plt.plot(x, myline)
plt.show()