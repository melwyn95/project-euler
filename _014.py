def exists(m, k):
    try:
        m[k]
        return True
    except: return False

answer, max_terms = -1, -1

def collatz_term(n, t, memo):
    if exists(memo, n): return memo[n]
    if n % 2 == 0: memo[n] = 1 + collatz_term(n // 2, t + 1, memo)
    else: memo[n] = 1 + collatz_term(3 * n + 1, t + 1, memo)
    terms = memo[n]
    global answer, max_terms
    if terms > max_terms: 
        max_terms = terms
        answer = n
    return terms

memo = { 1 : 1 }
N = 1000000

for n in range(1, N): collatz_term(n, 1, memo)

print(answer)