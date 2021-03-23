from utils import digits

def is_pandigital(xs):
    if len(xs) == 9:
        s = 0
        memo = [0 for _ in range(10)]
        for x in xs:
            if x == 0: return False
            if memo[x] == 0: memo[x] = 1
            else: return False
            s += x
        return s == 45
    return False

answer = 0
n = 1
while len(digits(n)) <= 5:
    pan = []
    p = 1
    while len(pan) < 9:
        pan += digits(p * n)
        p += 1
    if is_pandigital(pan):
        answer = max(answer, int("".join(map(str, pan))))
    n += 1

print(answer)
