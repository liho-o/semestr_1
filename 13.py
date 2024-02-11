import math
radius_1 = float(input("Радиус 1"))
radius_2 = float(input("Радиус 2"))

area_1 = math.pi * radius_1 * radius_1
area_2 = math.pi * radius_2 * radius_2

print(f"{math.fabs(area_1 - area_2)}")
