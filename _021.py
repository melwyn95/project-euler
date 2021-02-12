import math

N = 10000

def divisors(n):
    ds = []
    for d in range(1, int(math.sqrt(n)) + 1):
        if n % d == 0: 
            ds.append(d)
            x = n // d
            if x != d and x != n: ds.append(x)
    return ds

amicable_numbers = set()

for n in range(N):
    if n in amicable_numbers: continue
    m = sum(divisors(n))
    if m >= N or m == n: continue
    if n == sum(divisors(m)):
        amicable_numbers.add(n)
        amicable_numbers.add(m)

amicable_numbers = list(amicable_numbers)

print(sum(amicable_numbers))
