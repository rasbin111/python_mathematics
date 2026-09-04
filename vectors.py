import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("TkAgg")

origin = (0, 0)
v1= (-3, 3)
v2 = (-2, 1)
plt.quiver(origin[0], origin[1], v1[0], v1[1], units="xy", scale=1)
plt.quiver(origin[0], origin[1], v2[0], v2[1], units="xy", scale=1)
plt.quiver(origin[0], origin[1], v1[0] - v2[0], v1[1] - v2[1], units="xy", color="red", scale=1)
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.grid()
plt.show()
