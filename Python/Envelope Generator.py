import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-whitegrid')

fig = plt.figure()
ax = plt.axes()
x = np.linspace(-100, 100, 51)
print(x)
length = len(x)
ax.plot(x, -x)
ax.plot(x, x)
for i in range(int(length/2)):
    x1 = x[i]
    x2 = x[int(length/2) + i]
    y1 = -x[i]
    y2 = x[int(length/2) + i]
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1
    ax.plot(x, m * x + b)
plt.show()