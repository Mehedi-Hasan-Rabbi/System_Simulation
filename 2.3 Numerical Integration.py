import random
import numpy as np
import matplotlib.pyplot as plt

def fun(x):
    return x**3

low = 2
upper = 5


# Shortcut to make linspace
x = np.linspace(low, upper)
y = x**3
plt.title("$f(x) = x^3$")
plt.plot(x, y)
plt.show()

# Simulation start
x_point = []
y_point = []
n = 0
m = 0
n_simulation = 5000
rectangle_height = 150

for i in range(n_simulation):
    x = random.randint(low*100, upper*100)
    x = x / 100
    y = random.randint(0, rectangle_height)

    x_point.append(x)
    y_point.append(y)

    if y <= fun(x):
        m += 1
    n += 1


ans = (m / n) * (rectangle_height*(upper - low))
print("Simulated integral value = " , ans)
# Simulation end

dotx = []
doty = []

i = 0
h = 0.2

while i < upper*2:
    dotx.append(i)
    doty.append(fun(i))

    i += h

plt.plot(dotx, doty)
plt.scatter(x_point, y_point)
plt.show()