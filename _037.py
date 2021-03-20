from utils import seive, bin_search

N = 10 ** 6

primes = seive(N)
num_primes = len(primes)

def is_trucatable_prime_right(prime):
    while prime > 0:
        if bin_search(primes, 0, num_primes - 1, prime) == -1:
            return False
        prime //= 10
    return True

powers_10 = [10 ** i for i in range(10)]

def greatest_10_power(n):
    t = 1
    while n // 10 > 0:
        n //= 10
        t += 1
    return t - 1

def is_trucatable_prime_left(prime):
    while prime > 0:
        is_prime = bin_search(primes, 0, num_primes - 1, prime) >= 0
        if not is_prime: return False
        if prime < 10 and is_prime: return True
        p = greatest_10_power(prime)
        if p == 0: p = 1
        prime %= powers_10[p]
    return True

answer = 0

for prime in primes:
    if prime < 10: continue
    right = is_trucatable_prime_right(prime)
    left = is_trucatable_prime_left(prime)
    if right and left:
        answer += prime

print(answer)
