import functools
from utils import big_multiply 
 
N = 1000
answer = [1]

for _ in range(N): answer = big_multiply(answer, [2])


print(sum(answer))
