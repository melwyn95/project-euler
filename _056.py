from utils import big_multiply, digits, digits_to_int

N = 99
answer = 0

for a in range(1, N + 1):
    digs = digits(a)
    prev = digits(a)
    for _ in range(1, N + 1):
        prev = big_multiply(prev, digs)
        answer = max(answer, sum(prev))

print(answer)
