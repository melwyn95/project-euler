from utils import is_prime, last

def permute(xs):
    if len(xs) == 1:
        return [xs[0]]
    else:
        zs = []
        for i in range(len(xs)):
            x = xs[i]
            ys = list(xs[0:i] + xs[i+1:])
            xs_ = permute(ys)
            zs += list(map(lambda x_: x + x_, xs_))
        return zs

vals = [1, 2, 3, 4, 5, 6, 7]
vals = list(map(str, vals))
permutations = permute(vals)
permutations = list(map(int, permutations))

filtered_permutations = list(filter(is_prime, permutations))

print(last(filtered_permutations))

## Note: by trial and error found that for all pandigitals for size 8 & 9
## there is no prime, 7 is the largest size pandigital which has primes
