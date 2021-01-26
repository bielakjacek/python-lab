from joblib import Parallel, delayed
import multiprocessing
import random

minimum_value = 0
maximum_value = 10

inputs = [random.randint(minimum_value, maximum_value) for i in range(100)]
hist = {}

for element in range(minimum_value, maximum_value):
    number_of_instances = inputs.count(element)
    hist[element] = number_of_instances

print(hist)





