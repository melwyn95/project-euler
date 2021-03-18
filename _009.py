from utils import bin_search

N = 1000

squares = [x ** 2 for x in range(N + 1)]

for a in range(1, N):
    for b in range(a + 1, N):
        c2 = squares[a] + squares[b]
        c = bin_search(squares, 0, len(squares) - 1, c2)
        if c >= 0 and (a + b + c) == 1000:
            print(a * b * c)
            
            exit(0)
