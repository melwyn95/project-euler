from utils import seive

primes = seive(1000000)

def count_divisors(primes, n):
    count = 1
    for p in primes:
        if p > n: break
        n_, c = n, 0
        while n_ > 1 and n_ % p == 0:
            n_ = n_ // p
            c += 1
        if c > 0: count *= (c + 1)
    return count

n = 1
triangle_number = 1
while count_divisors(primes, triangle_number) < 500:
    n += 1
    triangle_number += n

print(triangle_number)
print("----")