import numpy as np
import matplotlib.colors as col
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Data for a three dimensional line
z = np.linspace(0, 15, 1000)
x = np.sin(z)
y = np.cos(z)

# Create a figure and an axes object
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Data for three dimensional scattered points
z = 15 * np.random.random(100)
x = np.sin(z) + 0.1 * np.random.randn(100)
y = np.cos(z) + 0.1 * np.random.randn(100)

# Plot the line and scattered points
ax.plot3D(x, y, z, 'grey')
ax.scatter3D(x, y, z, c=z, cmap='Greens')

# Display the plot
plt.show()
