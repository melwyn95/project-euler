N = 100

squares_sum = sum([x ** 2 for x in range(1, N + 1)])
sum_squared = ((N * (N + 1)) // 2) ** 2

print(sum_squared - squares_sum)