import math
import numpy as np

def distancebetween(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1) ** 2)


def distinput():
    x1 = float(input("First x coordinate")) 
    y1 = float(input("First x coordinate")) 
    x2 = float(input("First x coordinate")) 
    y2 = float(input("First x coordinate"))
    
    distance = distancebetween(x1, y1, x2, y2)
    
    return distance


def userexpr():
    distance = distinput()
    print("Distance between points is: ", distance)
userexpr()