import random

a = [[random.randint(0, 10) for i in range(128)] for j in range(128)]
b = [[random.randint(0, 10) for i in range(128)] for j in range(128)]
c = [[0 for i in range(128)] for j in range(128)]
for i in range(128):
    for j in range(128):
        c[i][j] = a[i][j] + b[i][j]

# Test
for i in range(128):
    for j in range(128):
        if c[i][j] != a[i][j] + b[i][j]:
            print("Adding failed.")
        else:
            pass

