from utils import seive, digits, digits_to_int

primes = seive(100000)
primes = list(filter(lambda x: x >= 1000 and x <= 9999, primes))

memo = {}

for prime in primes:
    key = digits_to_int(list(sorted(digits(prime))))
    if key in memo: memo[key].append(prime)
    else: memo[key] = [prime]

for ps in memo.values():
    m = {}
    for i in range(len(ps)):
        for j in range(i + 1, len(ps)):
            diff = abs(ps[i] - ps[j])
            if diff in m: 
                m[diff].add(ps[i])
                m[diff].add(ps[j])
            else:
                m[diff] = set([ps[i], ps[j]])
    for vs in m.values():
        if len(vs) == 3: 
            a, b, c = list(sorted(list(vs)))
            print(str(a) + str(b) + str(c))

        