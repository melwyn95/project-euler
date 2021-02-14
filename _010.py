from utils import seive

N = 2000000
primes = seive(N)

answer = sum(primes)

print(answer)
