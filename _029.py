from utils import fast_power

A = 100
B = 100

s = set()

for a in range(2, A + 1):
    for b in range(2, B + 1):
        s.add(fast_power(a, b))

print(len(list(s)))
