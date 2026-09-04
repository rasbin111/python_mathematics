import math
import matplotlib.pyplot as plt

def add_vector(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1])

def shrink_vector(factor, v):
    return (v[0]/factor, v[1]/factor)

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

def rotate(rotation_angle, vectors):
    polar_vectors = [to_polar(v) for v in vectors]
    rotated_polar_vectors = [(l, angle + rotation_angle) for l, angle in polar_vectors]
    rotated_vectors = [to_cartesian(p) for p in rotated_polar_vectors]
    return rotated_vectors

def translate(translate_coordinates, vectors):
    return [add_vector(translate_coordinates, v) for v in vectors]

def shrink(factor, vectors):
    return [shrink_vector(factor, v) for v in vectors]

dino_vectors = [(6,4), (3,1), (1, 2), (-1, 5), (-2, 5), (-3, 4), (-4, 4), (-5, 3), (-5, 2), (-2, 3),
                (-5, 1), (-4, 0), (-2, 1), (-1, 0), (0, -3), (-1, -4), (1, -4), (2, -3), (1, -2),
                (3, -1), (5, 1), (6, 4)]



xs = [p[0] for p in dino_vectors]
ys = [p[1] for p in dino_vectors]

fig, ax = plt.subplots(figsize=(8,8))
ax.fill(xs, ys, color="darkgreen", edgecolor="black", linewidth=1)
ax.set_aspect("equal")
ax.axis("off")
plt.show()



