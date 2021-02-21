
def right(count, pos, n):
    xs = []
    r, c = pos
    while n > 0:
        count += 1
        r += 1
        xs.append((count, (r, c)))
        n -= 1
    return xs
def down(count, pos, n):
    xs = []
    r, c = pos
    while n > 0:
        count += 1
        c -= 1
        xs.append((count, (r, c)))
        n -= 1
    return xs
def left(count, pos, n):
    xs = []
    r, c = pos
    while n > 0:
        count += 1
        r -= 1
        xs.append((count, (r, c)))
        n -= 1
    return xs
def up(count, pos, n):
    xs = []
    r, c = pos
    while n > 0:
        count += 1
        c += 1
        xs.append((count, (r, c)))
        n -= 1
    return xs

def last(xs):
    return xs[len(xs) - 1]

def second_last(xs):
    return xs[len(xs) - 2]

def is_diagonal(pos):
    r, c = pos
    return abs(r) == abs(c)

def spiral(n):
    c, times, initial = 1, 1, (0, 0)
    s = 0
    while True:
        ps = right(c, initial, times)
        
        xs = list(map(lambda ps: ps[0], filter(lambda ps: is_diagonal(ps[1]), ps)))
        if len(xs) > 0:
            s += xs[0]
        c, initial = last(ps)
        
        x, _ = second_last(ps)
        if n * n == x: break

        ps = down(c, initial, times)
        s += list(map(lambda ps: ps[0], filter(lambda ps: is_diagonal(ps[1]), ps)))[0]
        c, initial = last(ps)

        times += 1
        ps = left(c, initial, times)
        s += list(map(lambda ps: ps[0], filter(lambda ps: is_diagonal(ps[1]), ps)))[0]
        c, initial = last(ps)

        ps = up(c, initial, times)
        s += list(map(lambda ps: ps[0], filter(lambda ps: is_diagonal(ps[1]), ps)))[0]
        c, initial = last(ps)

        times += 1
    return s + 1
        
    
# print(spiral(1001))

def simple(n):
    s, diff = 1, 2
    answer = s

    while s != n * n:
        s += diff
        answer += s
        s += diff
        answer += s
        s += diff
        answer += s
        s += diff
        answer += s
        diff += 2
    
    return answer

print(simple(1001))
