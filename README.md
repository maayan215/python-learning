﻿# python-learning
Task:
git game
https://learngitbranching.js.org/
___________________________________________________________________

Task:
 Given a list of 2D points, find the best-fit line y = ax + b that minimizes the squared vertical distances from the points to the line (simple linear regression).


Visualization:
 Plot the points and the resulting line on the same graph.

___________________________________________________________________
Task:
 Given a set of 2D points, compute the convex hull (the smallest convex polygon that encloses all points). Use an algorithm like Jarvis March or Graham Scan.


Visualization:
 Plot all points and draw the convex hull polygon around them.

___________________________________________________________________
Task:
 You are given two rectangles defined either by corner coordinates or by origin and size. Compute the overlapping area between them (if any).


Visualization:
 Plot both rectangles and color the overlapping region differently.

___________________________________________________________________
Task:
 Given 3 points in 3D space, compute the normal vector to the plane formed by them (using the cross product).


Visualization:
 Use matplotlib’s 3D plotting tools to show the 3 points and the normal vector.

___________________________________________________________________
1. Base Class: Shape (Abstract)

class Shape:
    def area(self): pass
    def perimeter(self): pass
    def draw(self, ax): pass

2. Subclasses (with properties and methods):
Circle (center, radius)


Rectangle (bottom-left point, width, height)


Triangle (three points)


Polygon (list of points)
 Each subclass must:


Implement area() and perimeter()


Implement draw(ax) that draws it on a given matplotlib Axes object


3. Class: Canvas
Maintains a list of Shape objects


Methods:


add_shape(shape)


draw_all()


total_area(), total_perimeter()


Optional: remove_shape(id or index)
Bonus Features (Optional):
Unique ID for each shape


Method to rotate/scale a shape


Add colors or line styles


Save the canvas as an image


Export and load all shapes to and from JSON

___________________________________________________________________

___________________________________________________________________

___________________________________________________________________

___________________________________________________________________

___________________________________________________________________

___________________________________________________________________

River SIzes

You're given a two-dimensional array (a matrix) of potentially unequal height and width containing only 0s and 1s. Each 0 represents land, and each 1 represents part of a river. A river consists of any number of 1s that are either horizontally or vertically adjacent (but not diagonally adjacent). The number of adjacent 1s forming a river determines its size.
Note that a river can twist. In other words, it doesn't have to be a straight vertical line or a straight horizontal line; it can be L-shaped, for example.
Write a function that returns an array of the sizes of all rivers represented in the input matrix. 
The sizes don't need to be in any particular order.
Sample Input 
matrix = [
  [1, 0, 0, 1, 0],
  [1, 0, 1, 0, 0],
  [0, 0, 1, 0, 1],
  [1, 0, 1, 0, 1],
  [1, 0, 1, 1, 0],
]
Sample output



for me details and testing,read this https://www.algoexpert.io/questions/river-sizes


