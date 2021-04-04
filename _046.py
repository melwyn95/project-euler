from utils import seive

N = 10 ** 6
primes = seive(N)
numbers = [False if x % 2 == 0 else True for x in range(N + 1)]
numbers[1] = False
for p in primes: numbers[p] = False
sq2 = [2 * x * x for x in range(1, 1000)]
for p in primes:
    for sq in sq2:
        if p + sq < N:
            numbers[p + sq] = False

for i in range(N):
    if numbers[i]: 
        print(i)
        break
