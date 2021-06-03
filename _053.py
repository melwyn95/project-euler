MILLION = 10 ** 6
N = 100

def nCr(n, r):
    nr, dr = 1, 1
    for _ in range(r):
        dr *= r
        nr *= n
        n -= 1
        r -= 1
    return nr // dr

count = 0

for n in range(1, N + 1):
    for r in range(1, n):
        if nCr(n, r) > MILLION: count += 1

print(count)
