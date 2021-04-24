from utils import digits, digits_to_int

N = 1000

def trunc_add(xys):
    zs = []
    n = max(map(len, xys))
    carry = 0
    bail = False
    for i in range(n):
        t = carry
        for ys in xys:
            if i < len(ys): t += ys[i]
        if t >= 10: carry = t // 10
        else: carry = 0
        zs.append(t % 10)
        if len(zs) == 10:
            bail = True
            break
    if not bail:
        if carry > 0: zs.append(carry)
    return list(reversed(zs))

def trunc_multiply(xs, ys):
    zs = []
    for yi in range(len(ys) - 1, -1, -1):
        bail = False
        carry = 0
        z = [0 for i in range(len(ys) - 1 - yi)]
        for xi in range(len(xs) - 1, -1, -1):
            t = (xs[xi] * ys[yi]) + carry
            if t >= 0: carry = t // 10
            else: carry = 0
            z.append(t % 10)
            if len(z) == 10:
                zs.append(z)
                bail = True
                break
        if not bail:
            if carry > 0: z.append(carry)
            zs.append(z)
    return trunc_add(zs)

def trunc_pow(x, n):
    ys = digits(x)
    xs = digits(x)
    for _ in range(n - 1):
        ys = trunc_multiply(ys, xs)
    return ys

pows = []
for n in range(N + 1): pows.append(list(reversed(trunc_pow(n, n))))
answer = digits_to_int(trunc_add(pows))
print(answer)