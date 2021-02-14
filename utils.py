import functools

def big_add(a, b):
    c = 0
    an, bn = len(a) - 1, len(b) - 1
    x = []
    while an >= 0 and bn >= 0:
        s = a[an] + b[bn] + c
        if s > 9: c = s // 10
        else: c = 0
        x.append(s % 10)
        an -= 1
        bn -= 1
    while an >= 0:
        s = a[an] + c
        if s > 9: c = s // 10
        else: c = 0
        x.append(s % 10)
        an -= 1
    while bn >= 0:
        s = b[bn] + c
        if s > 9: c = s // 10
        else: c = 0
        x.append(s % 10)
        bn -= 1 
    if c > 0: x.append(c)
    return list(reversed(x))

def big_multiply(a, b):
    p = []
    for z, bi in enumerate(reversed(b)):
        c = 0
        pi = [0 for _ in range(z)]
        for ai in reversed(a):
            m = ai * bi + c
            pi.append(m % 10)
            c = m // 10
        while c > 0: 
            pi.append(c % 10)
            c //= 10
        p.append(list(reversed(pi)))
    return functools.reduce(big_add, p[1:], p[0])

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

def is_prime(n):
    if n < 0: return False
    i = 2
    while i * i < n:
        if n % i == 0: return False
        i += 1
    return True
