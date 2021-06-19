import math

def num_digits(n):
    return math.floor(math.log10(n)) + 1

def resolve(a, b, c):
    return [a * c + b, c]

def converge(times):
    initial = [1, 2]
    while times > 1:
        initial = resolve(2, initial[0], initial[1])
        initial.reverse()
        times -= 1
    return resolve(1, initial[0], initial[1])

times = 1000

answer = 0

for t in range(1, times + 1):
    n, d = converge(t)
    if num_digits(n) > num_digits(d): answer += 1

print(answer)