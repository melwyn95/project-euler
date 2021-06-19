import math
from utils import digits

def num_digits(n):
    return math.floor(math.log10(n)) + 1

answer = 0
N = 100

for n in range(N):
    m = 1
    mn = len(digits((pow(m, n))))
    while mn <= n:
        mn = len(digits((pow(m, n))))
        if mn == n:
            answer += 1
        m += 1

print(answer)

