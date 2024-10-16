# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 17:52:34 2024

@author: idilg
"""
import math

points = [
    ((1, 2), (4, 6)),  # 1. nokta çifti
    ((7, 0), (3, 4)),  # 2. nokta çifti
    ((-1, -1), (2, 3)),  # 3. nokta çifti
    ((2, 3), (5, 7))  # 4. nokta çifti
]
def euclideanDistance(points):
    (x1, y1), (x2, y2) = points
    distance = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    return distance

distances=[]
for i in points:
    distance = euclideanDistance(i)
    distances.append(distance)

distances.sort()

print(distances[0])