import random
import numpy


def create_matrix_minor(a, i, j):
    return [row[:j] + row[j + 1:] for row in (a[:i] + a[i + 1:])]


def calculate_det(a):
    if len(a[0]) == 2:
        return a[0][0] * a[1][1] - a[0][1] * a[1][0]
    det = 0
    for i in range(len(a[0])):
        det += ((-1) ** i) * a[0][i] * calculate_det(create_matrix_minor(a, 0, i))
    return det


# TEST

b = [[random.randint(0, 5) for i in range(8)] for j in range(8)]
check_det = numpy.linalg.det(b)
print(abs(calculate_det(b) - check_det) < 0.1)
