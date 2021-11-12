from typing import Tuple
from utils import digits

ones = set([1])
eighty_nines = set([89])

sq = lambda x: x * x
sum_digit_sqs = lambda n: sum(map(sq, digits(n)))

def resolve(n):
    if n in ones: return True
    elif n in eighty_nines: return False
    else:
        if resolve(sum_digit_sqs(n)): 
            ones.add(n)
            return True
        else: 
            eighty_nines.add(n)
            return False

for n in range(1, 10000000):
    resolve(n)
    pass

print(len(eighty_nines))