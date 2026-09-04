import matplotlib.pyplot as plt

dino_vectors = [(6,4), (3,1), (1, 2), (-1, 5), (-2, 5), (-3, 4), (-4, 4), (-5, 3), (-5, 2), (-2, 3), (-5, 1), (-4, 0), (-2, 1), (-1, 0),
                (0, -3), (-1, -4), (1, -4), (2, -3), (1, -2), (3, -1), (5, 1), (6, 4)]

xs = [p[0] for p in dino_vectors]
ys = [p[1] for p in dino_vectors]

plt.plot(xs, ys, color="m")

plt.grid(True)
plt.show()

