import math
import matplotlib.pyplot as plt

rotation_angle = math.pi / 4

def to_polar(cordinate):
    x, y = cordinate
    r = math.sqrt(x ** 2 + y ** 2)
    tr = math.atan2(y, x)
    return (r, tr)

def to_cartesian(polar_coordinate):
    r, theta = polar_coordinate
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return (x, y)

dino_vectors = [(6,4), (3,1), (1, 2), (-1, 5), (-2, 5), (-3, 4), (-4, 4), (-5, 3), (-5, 2), (-2, 3), (-5, 1), (-4, 0), (-2, 1), (-1, 0),
                (0, -3), (-1, -4), (1, -4), (2, -3), (1, -2), (3, -1), (5, 1), (6, 4)]

dino_polar = [to_polar(v) for v in dino_vectors]
dino_rotated_polar = [(l, angle + rotation_angle) for l, angle in dino_polar]
dino_rotated = [to_cartesian(p) for p in dino_rotated_polar]

xs = [p[0] for p in dino_vectors]
ys = [p[1] for p in dino_vectors]

xsr = [p[0] for p in dino_rotated]
ysr = [p[1] for p in dino_rotated]

plt.plot(xs, ys, color="gray")
plt.plot(xsr, ysr, color="r")

plt.grid(True)
plt.show()

