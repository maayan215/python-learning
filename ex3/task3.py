import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

fig, ax = plt.subplots()
def get_overlap_area(rect1, rect2):
    ((min_x1, min_y1), (max_x1, max_y1)) = rect1
    ((min_x2, min_y2), (max_x2, max_y2)) = rect2
    
    overlap_min_x = max(min_x1, min_x2)
    overlap_min_y = max(min_y1, min_y2)
    overlap_max_x = min(max_x1, max_x2)
    overlap_max_y = min(max_y1, max_y2)  
    
    overlap_redct_width = overlap_max_x - overlap_min_x
    overlap_redct_hight = overlap_max_y - overlap_min_y
    
    overlap_area = overlap_redct_hight * overlap_redct_width 
    if overlap_area < 0:
        overlap_area = 0    # no negative area
    
    return (overlap_min_x, overlap_min_y, overlap_redct_width, overlap_redct_hight, overlap_area)

def add_rect(rect, color):
    global ax
    ax.add_patch(Rectangle(rect[0], rect[1][0] - rect[0][0], rect[1][1] - rect[0][1], edgecolor=color, facecolor=color, alpha=0.3))

def max_value(rect1, rect2):
    return max(p[0] for p in rect1+rect2),  max(p[1] for p in rect1+rect2)

def show_rectangles(rect1, rect2, overlap_rect):
    global ax
    add_rect(rect1, 'green')
    add_rect(rect2, 'blue')
    if overlap_rect[2] > 0 and overlap_rect[3] > 0:
        ax.add_patch(Rectangle((overlap_rect[0], overlap_rect[1]), overlap_rect[2], overlap_rect[3], edgecolor='red', facecolor='red', alpha=0.5, label='Overlap'))
    
    ax.set_xlim(min(rect1[0][0], rect2[0][0]) - 1, max(rect1[1][0], rect2[1][0]) + 1)
    ax.set_ylim(min(rect1[0][1], rect2[0][1]) - 1, max(rect1[1][1], rect2[1][1]) + 1)
    
    plt.show()


# rect1 = ((1,1), (5,5))
# rect2 = ((3,3), (6,6))

rect1 = ((5, 0), (10, 4))
rect2 = ((11,1), (12,3.5))

overlapping_rect = get_overlap_area(rect1, rect2)
print(f"The overlapping Area is: {overlapping_rect[4]}")
show_rectangles(rect1, rect2, overlapping_rect)
