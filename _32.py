def digits(n):
    ds = []
    while n > 0:
        ds.append(n % 10)
        n //= 10
    return ds

def is_pandigital(a, b, p):
    cs = [0 for _ in range(10)]
    for d in a:
        if d == 0: return False
        cs[d] += 1
        if cs[d] >= 2: return False
    for d in b:
        if d == 0: return False
        cs[d] += 1
        if cs[d] >= 2: return False
    for d in p:
        if d == 0: return False
        cs[d] += 1
        if cs[d] >= 2: return False
    return sum(cs) == 9

def is_under_digit_limit(a, b, p):
    return len(a) + len(b) + len(p) <= 9

a, b = 1, 1

all_pandigial_products = []

unique_products = set()

while True:
    b = 1
    digits_a = digits(a)
    while True:
        p = a * b
        digits_b = digits(b)
        digits_p = digits(p)

        if is_pandigital(digits_a, digits_b, digits_p):
            print(a, b, p)
            all_pandigial_products.append((a, b, p))
            unique_products.add(p)

        if not is_under_digit_limit(digits_a, digits_b, digits_p):
            break                

        b += 1    
    if not is_under_digit_limit(digits_a, [1], digits_a):
        break
    a += 1

print(len(all_pandigial_products))

print(sum(unique_products))
