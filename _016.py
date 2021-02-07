import functools

from _013 import big_add

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
    
N = 1000
answer = [1]

for _ in range(N): answer = big_multiply(answer, [2])


print(sum(answer))
print("----")