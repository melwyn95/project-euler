from utils import bin_search

f = open("./inputs/_042", "r")
names = list(map(lambda s: s.replace('"', ''), f.read().strip().split(",")))

A = ord('A')

def of_name(name):
    return sum(map(lambda n: ord(n) - A + 1, name))

possibly_triangle_numbers = list(map(of_name, names))

n = 20
triangle_numbers = [int(0.5*n*(n+1)) for n in range(1, n)]
is_triangle_number = lambda x: bin_search(triangle_numbers, 0, len(triangle_numbers) - 1, x) >= 0

triangle_words = list(filter(is_triangle_number, possibly_triangle_numbers))

print(len(triangle_words))
