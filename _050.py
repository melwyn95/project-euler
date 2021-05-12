from utils import seive, bin_search

MILLION = 10 ** 6
primes = seive(MILLION)

N = len(primes)

sums = []
for i in range(N):
    if i - 1 < 0: sums.append(primes[i])
    else: sums.append(primes[i] + sums[i - 1])

answer = 0
terms = 0
for n in range(1, N - 1):
    for i in range(N - 1 - n):
        p = sums[i + n - 1]
        if i > 0: p -= sums[i]
        if p > MILLION: break
        if bin_search(primes, 0, N - 1, p) >=  0 and n > terms: 
            answer = p
            terms = n

print(answer)
