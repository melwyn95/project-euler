from utils import seive, digits, bin_search

def rotations(n):
    ds = digits(n)
    rots = [n]
    num = len(ds)
    f = 10 ** (num - 1)
    for _ in range(num - 1):
        n = n % f * 10 + n // f
        rots.append(n)
    return rots

N = 10 ** 6
primes = seive(N)
num_primes = len(primes)

num_circular_primes = 0

for prime in primes:
    rots = rotations(prime)
    is_circular_prime = True
    for rot in rots:
        if bin_search(primes, 0, num_primes - 1, rot) == -1:
            is_circular_prime = False
            break
    if is_circular_prime:
        num_circular_primes += 1

print(num_circular_primes)

