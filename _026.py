
def one_divide_by(n):
    N = 1
    ds = []
    while N < n: 
        N *= 10
        ds.append(0)
    ds.pop()
    count = 0
    found = set()
    while N % n != 0:
        if (N % n) not in found: 
            found.add(N % n)
            count += 1
            N = (N % n) * 10
        else: break

    return [count, n]

print(max(map(one_divide_by, range(2, 1000))))
