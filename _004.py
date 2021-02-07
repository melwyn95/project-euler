
def is_pallindrome(n):
    return int(str(n)[::-1]) == n

answer = -1

for a in range(999, 99, -1):
    for b in range(999, 99, -1):
        n = a * b
        if is_pallindrome(n) and n > answer:
            answer = n

print(answer)
print("----")