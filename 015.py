N = 20

grid = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(N + 1): grid[0][i] = grid[i][0] = 1

def sum_neighbours(x, y):
    return grid[x][y-1] + grid[x-1][y]

def explore(n):
    grid[n][n] = sum_neighbours(n, n)
    for i in range(n + 1, N + 1):
        grid[n][i] = sum_neighbours(n, i)
        grid[i][n] = sum_neighbours(i, n)

for i in range(1, N + 1): explore(i)

print(grid[N][N])