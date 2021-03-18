from utils import digits

def common(xs, ys):
    zs = []
    ws = []
    for x in xs:
        if x in ys:
            zs.append(x)
    for y in ys:
        if y in xs:
            ws.append(y)
    if len(zs) < len(ws): return zs
    return ws

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def reduce_fraction(n, d):
    g = gcd(n, d)
    return (n / g, d / g)

N, D = 1, 1
for n in range(1, 100):
    for d in range(1, 100):
        ns = digits(n)
        ds = digits(d)
        cs = common(ns, ds)
        if len(cs) > 0:
            for c in cs:
                ns.remove(c)
                ds.remove(c)
            new_n = 1 if len(ns) == 0 else ns[0]
            new_d = 1 if len(ds) == 0 else ds[0]
            new_n, new_d = reduce_fraction(new_n, new_d)
            if new_d == 0: continue
            new_div = new_n / new_d
            div = n / d
            if div == new_div and new_div < 1 and n % 10 != 0 and d % 10 != 0:
                N *= new_n
                D *= new_d

g = gcd(N, D)
print(D / g)
                
