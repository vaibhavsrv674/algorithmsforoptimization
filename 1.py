Practical No. 1 - Implement Contour Plots

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

X, Y = np.meshgrid(x, y)

Z = X**2 + Y**2

plt.contour(X, Y, Z)

plt.xlabel("X")
plt.ylabel("Y")

plt.title("Contour Plot of Z = X² + Y²")

plt.show()
