from utils import seive

primes = seive(1000000)

X = 600851475143

largest = -1

for p in primes:
    while X % p == 0:
        largest = p
        X = X // p

print(largest)
print("----")