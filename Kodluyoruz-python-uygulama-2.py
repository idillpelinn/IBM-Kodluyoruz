# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 17:52:34 2024

@author: idilg
"""
import math

# Noktaların Tanımlanması
points = [
    (1, 2),
    (4, 6),
    (0, 0),
    (3, 4),
    (-1, -1),
    (2, 3),
    (5, 7)
]

# Öklid Mesafesi İçin Fonksiyon
def euclideanDistance(point1, point2):
    (x1, y1) = point1
    (x2, y2) = point2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

# Mesafelerin Hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum Mesafenin Bulunması
min_distance = min(distances)
print(f"Minimum Mesafe: {min_distance}")
