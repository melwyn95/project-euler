MILLION = 10 ** 6

def digits(n):
    if n == 0: return {0:1}
    ds = {}
    while n > 0:
        d = n % 10
        if d in ds: ds[d] += 1
        else: ds[d] = 1
        n //= 10
    return ds

def check(a, b):
    for i in range(10):
        if i in a and i in b: 
            if a[i] != b[i]: return False
        elif i in a or i in b: return False
    return True

for n in range(1, MILLION + 1):
    ns = digits(n)
    nx2, nx3, nx4, nx5, nx6 = 2 * n, 3 * n, 4 * n, 5 * n, 6 * n
    a = digits(nx2)
    if check(ns, a):
        b = digits(nx3)
        if check(ns, b):
            c = digits(nx4)
            if check(ns, c):
                d = digits(nx5)
                if check(ns, d):
                    e = digits(nx6)
                    if check(ns, e): 
                        print(n)
                        break
