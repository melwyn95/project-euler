from utils import digits, big_multiply, digits_to_int

N = 1000
mod = 10 ** 10

def big_pow(n, x):
    ds = digits(n)
    acc = digits(n)
    for _ in range(x - 1):
        acc = big_multiply(acc, ds)
    return digits_to_int(acc) % mod

s = 0
for i in range(1, N + 1):
    print(i)
    s += big_pow(i, i)

print(s)
