from math import sqrt, floor

def is_pentagonal(pn):
    n = (1 + sqrt(1 + (24 * pn))) / 6
    return floor(n) == n

def is_triangle(tn):
    n = (-1 + sqrt(1 + (8 * tn))) / 2
    return floor(n) == n 

def is_hexagonal(hn):
    n = (1 + sqrt(1 + (8 * hn))) / 4
    return floor(n) == n 

def triangle(n):
    return n * (n + 1) // 2

x = 40755
n = 1
while True:
    tn = triangle(n)
    if is_hexagonal(tn) and is_pentagonal(tn) and tn > x:
        print(tn)
        break
    n += 1
