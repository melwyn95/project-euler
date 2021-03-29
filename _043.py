from utils import permute

primes = [2, 3, 5, 7, 11, 13, 17]
def are_substrings_divisible(s):
    if s[0] == "0": return False
    n = 7
    substrings = [int(s[1+i:1+i+3]) for i in range(n)]
    for i in range(n):
        if substrings[i] % primes[i] != 0: return False
    return True

vals = [i for i in range(10)]
vals = list(map(str, vals))

pandigitals = sum(map(int, filter(are_substrings_divisible, permute(vals))))

print(pandigitals == 16695334890)
