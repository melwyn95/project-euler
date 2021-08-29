triangle = lambda n: n * (n + 1) // 2
square = lambda n: n * n
pentagonal = lambda n: n * (3 * n - 1) // 2
hexagonal = lambda n: n * (2 * n - 1)
heptagonal = lambda n: n * (5 * n - 3) // 2
octagonal = lambda n: n * (3 * n - 2)

def make(fn):
    n = 1
    xs = []
    prefix, suffix = {}, {}
    while True:
        m = fn(n)
        if m >= 1000 and m <= 9999:
            xs.append(m)
            p, s = m // 100, m % 100
            if p in prefix: prefix[p].append(m)
            else: prefix[p] = [m]
            if s in suffix: suffix[s].append(m)
            else: suffix[s] = [m]
        elif m > 9999: break
        n += 1
    return xs, prefix, suffix

triangle_ns, triangle_prefix, triangle_suffix = make(triangle)
square_ns, square_prefix, square_suffix = make(square)
pentagonal_ns, pentagonal_prefix, pentagonal_suffix = make(pentagonal)
hexagonal_ns, hexagonal_prefix, hexagonal_suffix = make(hexagonal)
heptagonal_ns, heptagonal_prefix, heptagonal_suffix = make(heptagonal)
octagonal_ns, octagonal_prefix, octagonal_suffix = make(octagonal)

def solve_prefix(numbers, suffix, explored):
    if len(explored) == 6:
        first = numbers[0]
        last = numbers[5]
        if (first // 100) == (last % 100):
            print(sum(numbers))
    for typ in ["triangle", "square", "pentagonal", "hexagonal", "heptagonal", "octagonal"]:
        if typ == "triangle" and "triangle" not in explored:
            if suffix in triangle_prefix:
                for tri in triangle_prefix[suffix]:
                    solve_prefix(numbers + [tri], tri % 100, explored + ["triangle"])
        elif typ == "square" and "square" not in explored:
            if suffix in square_prefix:
                for sq in square_prefix[suffix]:
                    solve_prefix(numbers + [sq], sq % 100, explored + ["square"])
        elif typ == "pentagonal" and "pentagonal" not in explored:
            if suffix in pentagonal_prefix:
                for pen in pentagonal_prefix[suffix]:
                    solve_prefix(numbers + [pen], pen % 100, explored + ["pentagonal"])
        elif typ == "hexagonal" and "hexagonal" not in explored:
            if suffix in hexagonal_prefix:
                for hex in hexagonal_prefix[suffix]:
                    solve_prefix(numbers + [hex], hex % 100, explored + ["hexagonal"])
        elif typ == "heptagonal" and "heptagonal" not in explored:
            if suffix in heptagonal_prefix:
                for hep in heptagonal_prefix[suffix]:
                    solve_prefix(numbers + [hep], hep % 100, explored + ["heptagonal"])
        elif typ == "octagonal" and "octagonal" not in explored:
            if suffix in octagonal_prefix:
                for oct in octagonal_prefix[suffix]:
                    solve_prefix(numbers + [oct], oct % 100, explored + ["octagonal"])
        else: pass

def solve():
    for tri in triangle_ns:
        suffix = tri % 100
        solve_prefix([tri], suffix, ["triangle"])

    for sq in square_ns:
        suffix = sq % 100
        solve_prefix([sq], suffix, ["square"])

    for pen in pentagonal_ns:
        suffix = pen % 100
        solve_prefix([pen], suffix, ["pentagonal"])

    for hex in hexagonal_ns:
        suffix = hex % 100
        solve_prefix([hex], suffix, ["hexagonal"])
    
    for hep in heptagonal_ns:
        suffix = hep % 100
        solve_prefix([hep], suffix, ["heptagonal"])

    for oct in octagonal_ns:
        suffix = oct % 100
        solve_prefix([oct], suffix, ["octagonal"])
solve()