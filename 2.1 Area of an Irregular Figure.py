import random
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon

irregular = [(1, 1), (10, 95), (40, 70), (50, 50),(30,20)]
map = Polygon(irregular)

x_point = []
y_point = []
for i in irregular:
    a = i[0]
    b = i[1]
    x_point.append(a)
    y_point.append(b)

x_point.append(x_point[0])
y_point.append(y_point[0])
plt.plot(x_point, y_point, color = "black")

# Enclose the irregular fig. in a khnow 50 * 100 rectangle
n = 0
m = 0
for i in range(2000):
    x = random.randint(0, 50)
    y = random.randint(0, 100)
    point = Point(x, y)

    if (map.contains(point)):
        m = m + 1
    n = n + 1

    plt.scatter(x, y)

plt.show()
print("Actual Area of Irregular Figure: ",map.area)
print("Predicted Area : ", (m/n)*(100*50))