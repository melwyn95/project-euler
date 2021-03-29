from utils import is_prime, last, permute

vals = [1, 2, 3, 4, 5, 6, 7]
vals = list(map(str, vals))
permutations = permute(vals)
permutations = list(map(int, permutations))

filtered_permutations = list(filter(is_prime, permutations))

print(last(filtered_permutations))

## Note: by trial and error found that for all pandigitals for size 8 & 9
## there is no prime, 7 is the largest size pandigital which has primes
