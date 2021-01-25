import numpy as np

list_to_sort = np.random.randint(100, size=50)
print(list_to_sort)
n = len(list_to_sort)
for i in range(n-1):
    for j in range(n-i-1):
        if list_to_sort[j] > list_to_sort[j+1]:
            list_to_sort[j], list_to_sort[j+1] = list_to_sort[j+1], list_to_sort[j]
print(list_to_sort)
