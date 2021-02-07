from _016 import big_add, big_multiply

def factorial(n):
    if n == 0: return [1]
    n_list = list(map(int, list(str(n))))
    return big_multiply(n_list, factorial(n-1))

print(sum(factorial(100)))
print("----")