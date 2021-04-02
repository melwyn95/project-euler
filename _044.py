from math import sqrt, floor

def is_pentagonal(pn):
    n = (1 + sqrt(1 + (24 * pn))) / 6
    return floor(n) == n

def pentagon(n):
    return n *(3 * n - 1) / 2

n = 10000

for a in range(1, n):
    for b in range(a + 1, n):
        if a == b: continue
        an = pentagon(a)
        bn = pentagon(b)
        if is_pentagonal(an + bn) and is_pentagonal(abs(an - bn)):
            print(abs(an - bn))
