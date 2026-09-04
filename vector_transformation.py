import math
import matplotlib.pyplot as plt

def add_vector(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1])

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
    polar_vectors = [to_polar(v) for v in dino_vectors]
    rotated_polar_vectors = [(l, angle + rotation_angle) for l, angle in polar_vectors]
    rotated_vectors = [to_cartesian(p) for p in rotated_polar_vectors]
    return rotated_vectors

def translate(transalte_coordinates, vectors):
    vectors = [add_vector(transalte_coordinates, v) for v in vectors]
    return vectors


dino_vectors = [(6,4), (3,1), (1, 2), (-1, 5), (-2, 5), (-3, 4), (-4, 4), (-5, 3), (-5, 2), (-2, 3), (-5, 1), (-4, 0), (-2, 1), (-1, 0),
                (0, -3), (-1, -4), (1, -4), (2, -3), (1, -2), (3, -1), (5, 1), (6, 4)]

dino_translated = translate((8,8), rotate(5 * math.pi/3, dino_vectors))

xs = [p[0] for p in dino_vectors]
ys = [p[1] for p in dino_vectors]


xst = [p[0] for p in dino_translated]
yst = [p[1] for p in dino_translated]

plt.plot(xs, ys, color="gray")
plt.plot(xst, yst, color="r")

plt.grid(True)
plt.show()

