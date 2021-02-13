from utils import big_add

N = 1000

f1 = [1]
f2 = [1]

fn = []
index = 2

while len(fn) < N: 
    fn = big_add(f1, f2)
    f1, f2 = f2, fn
    index += 1

print(index)