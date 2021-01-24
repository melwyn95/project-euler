N = 4000000

fib = [1, 2]
count = 2
answer = 2

def f(i):
    s = fib[i-1] + fib[i-2]
    fib.append(s)
    return s

while fib[count - 1] <= N:
    s = f(count)
    if s % 2 == 0: answer += s
    count += 1 

print(answer)