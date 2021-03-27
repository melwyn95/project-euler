from utils import digits

MILLION = 10 ** 6

n = 0
m = 0

answer = 1

interesting_indices = [10 ** i for i in range(1, 7)]

def some(fn, xs):
    for i, x in enumerate(xs):
        if fn(x): return i, True
    return -1, False

while n < MILLION: 
    m += 1
    digits_ = digits(m)
    len_digits_ = len(digits_)
    n += len_digits_
    ind, interesting = some(lambda ind: n >= ind, interesting_indices)
    if interesting:
        interesting_index = interesting_indices.pop(ind)
        answer *= digits_[len_digits_ - n + interesting_index - 1]
        
print(answer)
