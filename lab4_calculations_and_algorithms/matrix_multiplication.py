import random
import numpy

a = [[random.randint(0, 10) for i in range(8)] for j in range(8)]
b = [[random.randint(0, 10) for i in range(8)] for j in range(8)]
c = [[0 for i in range(8)] for j in range(8)]

for i in range(8):
    for j in range(8):
        for k in range(8):
            c[i][j] += a[i][k] * b[k][j]

# TEST
c_check = numpy.matmul(a, b)
for i in range(8):
    for j in range(8):
        if c[i][j] != c_check[i][j]:
            print("Failed.")