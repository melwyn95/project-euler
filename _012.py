import math

def divisors(n):
    ds = []
    for d in range(1, int(math.sqrt(n)) + 1):
        if n % d == 0: 
            ds.append(d)
            x = n // d
            if x != d: ds.append(x)
    return ds

n = 1
triangle_number = 1
while len(divisors(triangle_number)) < 500:
    n += 1
    triangle_number += n

print(triangle_number)
