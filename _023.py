import math

def divisors(n):
    ds = []
    for d in range(1, int(math.sqrt(n)) + 1):
        if n % d == 0: 
            ds.append(d)
            x = n // d
            if x != d and x != n: ds.append(x)
    return ds

N = 28123

def calc_abundant_numbers(N):
    abundant_numbers = []
    for i in range(1, N + 1):
        if sum(divisors(i)) > i:
            abundant_numbers.append(i)
    return abundant_numbers


abundant_numbers = calc_abundant_numbers(N)
an = len(abundant_numbers)

answer = N * (N + 1) // 2

memo = set()
for i in range(an):
    for j in range(i, an):
        a = abundant_numbers[i]
        b = abundant_numbers[j]
        if a + b <= N and a + b not in memo:
            memo.add(a + b)
            answer -= (a + b)

print(answer)