from utils import digits

f = open("./inputs/_079", "r")

codes = list(map(lambda n: digits(int(n)), f.read().split("\n")))

dependencies = {}

occurs = set()

for i in range(10): dependencies[i] = set()

for code in codes:
    for i in range(3):
        occurs.add(code[i])
        for j in range(i + 1, 3):
            dependencies[code[i]].add(code[j])

possible = set()

def traverse(i, n):
    if len(dependencies[i]) == 0: 
        global possible
        possible.add(n)
    else:
        for j in dependencies[i]:
            traverse(j, n * 10 + j)

for i in range(10):
    traverse(i, i)

possible = list(possible)
possible.sort()

for p in possible:
    pi = digits(p)
    if len(pi) == len(occurs):
        print(p)