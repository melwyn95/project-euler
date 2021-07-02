from utils import is_prime

level = 2
number = 1

prime = 0
count = 1

threshold = 0.10

while level < 100000:
    for idx in range(4):
        number += level
        if idx < 3 and is_prime(number): prime += 1
        count += 1
    level += 2
    if (prime / count) < threshold: 
        print(level - 1)
        break
