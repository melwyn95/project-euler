from utils import digits

N = 10 ** 6

def is_palindrome(xs):
    size = len(xs)
    if size == 1: return True
    for i in range(size // 2):
        if xs[i] != xs[size - 1 - i]:
            return False
    return True

def base2(n):
    binary = []
    while n > 0:
        binary += [n % 2]
        n //= 2
    return binary

answer = 0

for n in range(N):
    if is_palindrome(digits(n)) and is_palindrome(base2(n)):
        answer += n

print(answer)
