f = open("./inputs/_081", "r")

m = list(map(lambda x: list(map(int, x.split(","))), f.read().split("\n")))

n = len(m)

cache = [[0 for _ in range(n)] for _ in range(n)]
cache[n - 1][n - 1] = m[n - 1][n - 1]
for i in range(n - 2, -1, -1): 
    cache[n - 1][i] = cache[n - 1][i + 1] + m[n - 1][i]
    cache[i][n - 1] = cache[i + 1][n - 1] + m[i][n - 1]

for i in range(n - 2, -1, -1):
    for j in range(n - 2, -1, -1):
        cache[i][j] = m[i][j] + min(cache[i + 1][j], cache[i][j + 1])

print(cache[0][0])