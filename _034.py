from utils import digits

answer = 0

factorials = []
for i in range(10): factorials.append(1 if i == 0 else i * factorials[i - 1])

N = sum(factorials)
for n in range(N + 1):
    ds = digits(n)
    if len(ds) > 1:
        if n == sum(map(lambda d: factorials[d], ds)):
            answer += n

print(answer)
