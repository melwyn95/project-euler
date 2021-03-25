P = 1000 + 1

max_p, max_solns = -1, -1
for p in range(P):
    solns = 0
    for a in range(1, (p // 3) + 2):
        for b in range(a, ((p - a) // 2) + 2):
            c = (p - (a + b))
            if b + c > a and abs(b - c) < a and a + c > b and abs(a - c) < b:
                a2, b2, c2 = a**2, b**2, c**2
                if a + b + c == p and ((a2 + b2 == c2) or (b2+c2==a2) or (c2+a2==b2)):
                    solns += 1
    if solns > max_solns:
        max_solns = solns
        max_p = p

print(max_p, max_solns)

# Better solution work throught all the right angled triangles and see which perimeter has maximum solutions
