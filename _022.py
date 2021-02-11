f = open("./inputs/_022", "r")
names = list(map(lambda s: s.replace('"', ''), f.read().split(",")))

def merge_sort(a, s, e, cmp):
    if s == e: return [a[s]]
    if s < e:
        m = (s + e) // 2
        xs = merge_sort(a, s, m, cmp)
        ys = merge_sort(a, m + 1, e, cmp)
        zs = []
        ni, nj, i, j = len(xs), len(ys), 0, 0
        while i < ni and j < nj:
            if cmp(xs[i], ys[j]) == -1:
                zs.append(xs[i])
                i += 1
            else:
                zs.append(ys[j])
                j += 1
        while i < ni: 
            zs.append(xs[i])
            i += 1
        while j < nj: 
            zs.append(ys[j])
            j += 1
        return zs
    return []

def str_cmp(x, y):
    nx, ny, i, j = len(x), len(y), 0, 0
    while i < nx and j < ny:
        if x[i] > y[j]: return 1
        if x[i] < y[j]: return -1
        if x[i] == y[j]:
            i += 1
            j += 1
    if (nx - i) == (ny - j): return 0
    if (nx - i) < (ny - j): return -1
    return 1

names = merge_sort(names, 0, len(names) - 1, str_cmp)

def char_number(c):
    return ord(c) - ord('A') + 1

def str_score(s, i):
    return (i + 1) * sum(map(char_number, list(s)))

answer = 0

for i, name in enumerate(names):
    answer += str_score(name, i)

print(answer)