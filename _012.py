def seive(N):
    numbers = [i for i in range(N + 1)]
    primes = []
    numbers[0] = numbers[1] = False
    numbers[2] = True
    for n in range(2, N + 1):
        if numbers[n]:
            primes.append(n)
            p = 2 * n
            while p < N + 1:
                numbers[p] = False
                p += n
    return primes

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