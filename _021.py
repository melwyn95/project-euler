N = 10000

def divisors(n):
    d = []
    for x in range(n//2, 0, -1):
        if n % x == 0:
            d.append(x)
    return d

amicable_numbers = set()

for n in range(N):
    if n in amicable_numbers: continue
    m = sum(divisors(n))
    if m >= N or m == n: continue
    if n == sum(divisors(m)):
        amicable_numbers.add(n)
        amicable_numbers.add(m)

amicable_numbers = list(amicable_numbers)

print(sum(amicable_numbers))
