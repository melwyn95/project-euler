from utils import seive, is_prime

primes = seive(1000)

def eqn(a, b, n):
    return n*n + a*n + b

max_primes, a_, b_ = 0, 0, 0

for a in range(1000):
    for b in primes:
        n = 0
        while is_prime(eqn(a, b, n)): n += 1
        if n > max_primes:
            max_primes = n
            a_ = a
            b_ = b
        n = 0
        while is_prime(eqn(-a, b, n)): n += 1
        if n > max_primes:
            max_primes = n
            a_ = -a
            b_ = b
        n = 0
        while is_prime(eqn(a, -b, n)): n += 1
        if n > max_primes:
            max_primes = n
            a_ = a
            b_ = -b
        n = 0
        while is_prime(eqn(-a, -b, n)): n += 1
        if n > max_primes:
            max_primes = n
            a_ = -a
            b_ = -b

print(a_ * b_)
