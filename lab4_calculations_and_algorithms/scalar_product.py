def scalar_product(a = [], b = []):
    sum = 0
    if len(a) == len(b):
        for i in range(len(a)):
            sum += a[i]*b[i]
        return sum

    else:
        return "Lengths does not match"

print(scalar_product([1, 2], [3, -5]))