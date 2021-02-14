from utils import seive

N = 20

primes = seive(N)

xs = []
for p in primes:
    q = p
    while q < N:
        q *= p
    xs.append(q // p)

import functools 

answer = functools.reduce(lambda x, y: x*y, xs, 1)

print(answer)
print("----")