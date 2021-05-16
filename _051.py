from utils import digits, digits_to_int

MILLION = 10 ** 6

_numbers = [i for i in range(MILLION + 1)]
_numbers[0] = _numbers[1] = False
_numbers[2] = True

def seive():
    primes = []
    for n in range(2, MILLION + 1):
        if _numbers[n]:
            primes.append(n)
            p = 2 * n
            while p < MILLION + 1:
                _numbers[p] = False
                p += n
    return primes

def lowest_n_digit_number(n):
    return 10 ** (n - 1)

primes = seive()
n_primes = len(primes)

def indices_to_replace(n):
    N = len(str(n))
    indices = []
    prev = [[i] for i in range(N)]
    x = 0
    while x <= N - 1:
        curr = []
        for p in prev:
            for j in range(p[len(p) - 1] + 1, N):
                curr.append(p + [j])
        indices += prev
        prev = curr
        x += 1 
    return indices

def replace_indices(indices, n):
    ds = digits(n)
    lowest = lowest_n_digit_number(len(ds))
    numbers = []
    for i in range(10):
        for ind in indices:
            ds[ind] = i
        n = digits_to_int(ds)
        if n > lowest:
            numbers.append(n)
    return numbers

def how_many_prime(numbers):
    p, first = 0, -1
    for n in numbers:
        if _numbers[n]: p += 1
        if first == -1 and _numbers[n]: first = n
    return p, first

for n in range(1, MILLION, 2):
    for indices in indices_to_replace(n):
        numbers = replace_indices(indices, n)
        p, smallest = how_many_prime(numbers)
        if p == 8:
            print(smallest)
            exit(0)
