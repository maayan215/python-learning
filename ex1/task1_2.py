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

def linear_regression(points: np.ndarray) -> tuple[float, float]:
  """returns the two factors of a liniar line, the slope and the interception point

  Args:
      points (np.array): np array of 2D points

  Returns:
      tuple[float, float]: The slope (m) and intercept (b) of the best-fit line.
  """
  
  x = points[:, 0]
  y = points[:, 1]
  
  # correlation coffeition
  correlation = pd.DataFrame.corr(pd.DataFrame(points)).loc[1][0]
  
  # the standart diviation
  std_x = np.std(x)
  std_y = np.std(y)
  
  # the slope of the line, m
  slope = ((std_y/std_x) * correlation)
  
  # the interception point with the y axies, b
  intercept = np.mean(y) - slope * np.mean(x) 
  
  return slope, intercept

m, intercept = linear_regression(points)

def line(x):
    return m * x + intercept

myline = list(map(line, x))

plt.scatter(x, y)
plt.plot(x, myline)
plt.show()