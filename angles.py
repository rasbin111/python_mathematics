import math

def to_cartesian(polar_vector):
    length, angle = polar_vector[0], polar_vector[1]
    return (length * math.cos(angle), length * math.sin(angle))

# print(math.tan(37))
# print(math.tan(116.57))
# print(math.tan(math.pi/4))
# print(math.tan(200))

angle = 37 * math.pi / 180
corodinates = to_cartesian((5, angle))
print(f"Cordinates from polar corodinates (5, {angle}): {corodinates}")


c2 = (-2, 3)

# Convert c2 to polar co-ordinates

# distance (r)
r = math.sqrt(c2[0]**2 + c2[1]**2)

sin_theta = 3/r

angle_radian = math.asin(sin_theta)

angle_degree = 180 / math.pi * angle_radian

# gives wrong angle
print(f"Polar corodinates from c2(-2, 3) is: ({r}, {angle_degree})")

correct_angle_radian = math.atan2(c2[1], c2[0]) # atan2(y, x)
angle_degree = 180 / math.pi * correct_angle_radian


print(f"Polar corodinates from c2(-2, 3) is: ({r}, {angle_degree})")
