import numpy as np
import matplotlib.pyplot as plt
import math


def distance(p1, p2):
    """calculate the distance between two points"""
    x1, y1, x2, y2 = *p1, *p2
    return math.sqrt((y2-y1)**2 + (x2-x1)**2)

def polar_angle(p1, p2):
    """calculate the poler angle between p1 and p2"""
    if p1[1] == p2[1]:
        return -math.pi
    dy = p1[1]-p2[1]
    dx = p1[0]-p2[0]
    return math.atan2(dy, dx)

def orientation(p1, p2, p3):
    """
    return the oriantation of the points (p1, p2, p3).
    1 if counter-clockwise, -1 if clockwise, 0 if linear.
    """
    x1, y1, x2, y2, x3, y3 = *p1, *p2, *p3
    d = (y3-y2)*(x2-x1) - (y2-y1)*(x3-x2)
    if d > 0:
        return 1
    elif d < 0:
        return -1
    else:
        return 0

def graham_scan(points):
    """
    get the convex hull of a set of 2D points using Graham scan algorithm.

    Args:
        points (list of [x, y]): Input points

    Returns:
        list of [x, y]: orderd list of the points form the convex hull
    """
    p0 = min(points, key=lambda p: (p[1], p[0]))
    points.sort(key=lambda p: (polar_angle(p0, p), distance(p0, p)))
    hull = []
    
    for i in range(len(points)):
        while len(hull) >= 2 and orientation(hull[-2], hull[-1], points[i]) != 1:
            hull.pop()
        hull.append(points[i])
    
    hull.append(hull[0]) # close the polygon
    return hull

points = [
    [2, 4],
    [3, 4],
    [3, 0],
    [2, 2],
    [4, 1],
    [1, 2],
    [5, 0],
    [3, 1],
    [1, 2],
    [0, 2]
]

# for i in range(len(points)):
#     plt.scatter(points[i][0], points[i][1])

# hull = np.array(graham_scan(points))

# plt.plot(hull[:, 0], hull[:, 1])

# plt.show()