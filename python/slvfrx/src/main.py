import math

def find_x(x):
    angle_PRQ = 135
    angle_UST = 15 * (x + 2)

    result = angle_PRQ + angle_UST

    return result


x_values = [-1, 7, 9, 13]
for x in x_values:
    print(f"Testing x = {x}, result = {find_x(x)}")
    if find_x(x) == 180:
        print(f"x = {x}")
        break
if find_x(x) == 180:
    print("x = 1")
else:
    print("no valid x found")