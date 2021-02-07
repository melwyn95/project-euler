N = 1000

squares = [x ** 2 for x in range(N + 1)]


def bin_search(a, s, e, x):
    if s <= e:
        m = (s + e) // 2
        if a[m] == x: return m
        elif x > a[m]: return bin_search(a, m + 1, e, x)
        else: return bin_search(a, s, m - 1, x) 
    return -1

for a in range(1, N):
    for b in range(a + 1, N):
        c2 = squares[a] + squares[b]
        c = bin_search(squares, 0, len(squares) - 1, c2)
        if c >= 0 and (a + b + c) == 1000:
            print(a * b * c)
            print("----")
            exit(0)