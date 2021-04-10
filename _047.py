from utils import seive, is_prime

N = 10 ** 6

DISTINCT_PRIME_FACTORS = 4

primes = seive(N)

def factorize(n):
    factors = set()
    i = 0
    prime = primes[i]
    while n > 1:
        if i > 100 and is_prime(n): 
            factors.add(n)
            break
        if n % prime == 0: 
            factors.add(prime)
            n //= prime
        else: 
            i += 1
            prime = primes[i]
    return list(factors)

cons, idx, len_cons = [], -1, 0
for n in range(1, N + 1):
    factors = factorize(n)
    if len_cons == DISTINCT_PRIME_FACTORS: break
    if len(factors) == DISTINCT_PRIME_FACTORS:
        if len_cons > 0:
            if cons[idx] + 1 == n:
                cons.append(n)
                idx += 1
                len_cons += 1
            else:
                cons = [n]
                idx = 0
                len_cons = 1
        else:
            cons = [n]
            idx = 0
            len_cons = 1
print(cons)
