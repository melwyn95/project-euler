tree = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
]

class Node:
    def __init__(self, x):
        self.x = x
        self.left = None
        self.right = None
    def setLeft(self, node):
        self.left = node
    def setRight(self, node):
        self.right = node


def make(tree):
    depth = len(tree)
    tree = list(map(lambda xs: list(map(Node, xs)), tree))
    for i, ns in enumerate(tree):
        if i + 1 == depth: continue
        for j, n in enumerate(ns):
            n.setLeft(tree[i + 1][j])
            n.setRight(tree[i + 1][j + 1])
    return tree[0][0]

tree = make(tree)

answer = 0

def max_path_sum(node, s):
    if node == None: 
        global answer
        if s > answer: answer = s
        return
    max_path_sum(node.left, s + node.x)
    max_path_sum(node.right, s + node.x)

print(max_path_sum(tree, 0))

print(answer)