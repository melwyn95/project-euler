def seive(N):
    numbers = [i for i in range(N + 1)]
    primes = []
    numbers[0] = numbers[1] = False
    numbers[2] = True
    for n in range(2, N + 1):
        if numbers[n]:
            primes.append(n)
            p = 2 * n
            while p < N + 1:
                numbers[p] = False
                p += n
    return primes


primes = seive(1000000)

X = 600851475143

largest = -1

for p in primes:
    while X % p == 0:
        largest = p
        X = X // p

print(largest)