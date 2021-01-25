import numpy as np


def roots(a, b, c):
    delta = b ** 2 - 4 * a * c
    sqrt_delta = np.sqrt(delta)
    if delta > 0:
        x1 = (-b + sqrt_delta) / 2 * a
        x2 = (-b - sqrt_delta) / 2 * a
        return [x1, x2]
    elif delta == 0:
        return -b / 2 * a
    else:
        return "No non-imaginary results."

print(roots(4,-7,1))
