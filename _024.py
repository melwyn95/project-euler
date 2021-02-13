def factorial(n):
    if n == 0: return 1
    return n * factorial(n - 1)

def nth_permuration(n, xs):
    s = len(xs) - 1
    permutation = []
    while s >= 0:
        f = factorial(s)
        lower = 1
        while f * lower < n: lower += 1
        n -= f * (lower - 1)
        permutation.append(xs[lower - 1])
        xs.pop(lower - 1)
        s -= 1
    return permutation

xs = list(range(10))
perm = nth_permuration(1000000, xs)

print("".join(map(str, perm)))