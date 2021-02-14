N = 1000
div_3 = sum([i for i in range(3, N, 3)])
div_5 = sum([i for i in range(5, N, 5)])
div_15 = sum([i for i in range(15, N, 15)])

print(div_3 + div_5 - div_15)
