
from utils import digits, fast_power

answer = 0

N = 5

upper_limit = (9 ** 5) * 5

pows = [fast_power(i, N) for i in range(10)]

for n in range(upper_limit):
    ds = digits(n)
    if sum(map(lambda d: pows[d], ds)) == n:
        answer += n
        
print(answer - 1)
