coins = [1, 2, 5, 10, 20, 50, 100, 200]

N = 200

memo = [[1 if c == 0 else 0 for _ in range(N + 1)] for c in range(len(coins))]

for i in range(1, len(coins)):
    for n in range(N + 1):
        if n - coins[i] >= 0:
            memo[i][n] += memo[i][n - coins[i]]
        memo[i][n] += memo[i - 1][n]

print(memo[len(coins) - 1][N])