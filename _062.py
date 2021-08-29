from utils import digits

N = 10 ** 6
Q = 5

def cube(n):
  c = n * n * n
  d = sorted(digits(c))
  d = "".join(list(map(str, d)))
  return c, d

memo = {}

for n in range(1, N + 1):
  n, d = cube(n)
  if d in memo:
    if len(memo[d]) + 1 == Q: 
      print(memo[d][0])
      break
    memo[d].append(n)
  else: 
    memo[d] = [n]
  