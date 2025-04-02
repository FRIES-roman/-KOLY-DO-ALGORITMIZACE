import random
import matplotlib.pyplot as plt

def monte_carlo_area(n=100000):
    inside_triangle = 0
    points_in_triangle = []
    points_outside_triangle = []
    
    for _ in range(n):
        x, y = random.uniform(0, 10), random.uniform(0, 10) 
        if x + y <= 10:  
            inside_triangle += 1
            points_in_triangle.append((x, y))
        else:
            points_outside_triangle.append((x, y))
    
    square_area = 100  
    triangle_area = (inside_triangle / n) * square_area  
    
    return triangle_area, points_in_triangle, points_outside_triangle

estimated_area, points_in_triangle, points_outside_triangle = monte_carlo_area()

