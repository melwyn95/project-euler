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
    if n < 0 or n == 1: return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True

def digits(n):
    if n == 0: return [0]
    ds = []
    while n > 0:
        ds.append(n % 10)
        n //= 10
    return list(reversed(ds))

def digits_to_int(ds):
    n, i = 0, 1
    for d in range(len(ds) - 1, -1, -1):
        n += ds[d] * i
        i *= 10
    return n

def big_num_to_string(bn):
    return "".join(map(str, bn))

def fast_power(a, n):
    if n == 0: return 1
    if n == 1: return a
    if n % 2 == 0:
        p = fast_power(a, n // 2)
        return p * p
    else:
        p = fast_power(a, (n - 1) // 2)
        return p * p * a
        
def bin_search(a, s, e, x):
    if s <= e:
        m = (s + e) // 2
        if a[m] == x: return m
        elif x > a[m]: return bin_search(a, m + 1, e, x)
        else: return bin_search(a, s, m - 1, x) 
    return -1

def last(xs):
    length = len(xs)
    return xs[length - 1]

def permute(xs):
    if len(xs) == 1:
        return [xs[0]]
    else:
        zs = []
        for i in range(len(xs)):
            x = xs[i]
            ys = list(xs[0:i] + xs[i+1:])
            xs_ = permute(ys)
            zs += list(map(lambda x_: x + x_, xs_))
        return zs
