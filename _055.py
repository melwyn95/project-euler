N = 10000

numbers = range(1, N + 1)

def reverse(n):
    m = 0
    while n > 0:
        m *= 10
        m += n % 10
        n //= 10
    return m

def is_pallindrome(n): 
    return n == reverse(n)

def is_lychrel_number(n, depth=0):
    if depth > 50: return False
    m = reverse(n)
    if is_pallindrome(m + n): return True
    return is_lychrel_number(m + n, depth=depth + 1)

lychrel_numbers = list(filter(lambda n: not is_lychrel_number(n), numbers))

print(len(lychrel_numbers))
