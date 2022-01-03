
def is_greater(a, an, b, bn):
    if an == bn:
        return (a / b) > 0
    p = min(an, bn)
    if p == bn:
        b = (a / b)
        bn = p
        an = an - p
        while an > 0 and bn > 0:
            if an < bn:
                a = a * b
                bn = bn - an
            else:
                b = a * b
                an = an - bn
        if a < 1 or b < 1: return False
        return True
    else:
        a = (a / b)
        an = p
        b = (1 / b)
        bn = bn - p
        while an > 0 and bn > 0:
            if an < bn: 
                a = a * b
                bn = bn - an
            else: 
                b = a * b
                an = an - bn
        if a < 1 or b < 1: return False
        return True

f = open("./inputs/_099", "r")
lines = f.readlines()
lines = list(map(lambda x: x[:len(x)-1], lines))
numbers = list(map(lambda line: line.split(","), lines))
numbers = list(map(lambda line: list(map(int, line)), numbers))

max_line = None
max_number = None

for i in range(len(numbers)):
    if max_number == None:
        max_number = numbers[i]
        max_line = i + 1
    else:
        a, an = max_number[0], max_number[1]
        b, bn = numbers[i][0], numbers[i][1]
        if not is_greater(a, an, b, bn):
            max_number = numbers[i]
            max_line = i + 1

print(max_line)
