from utils import seive, is_prime

N = 10 ** 4
primes = seive(N)
primes = primes[1:]

n_primes = len(primes)

def check_prime_cocatenation(a, b):
    return is_prime(int(a + b)) and is_prime(int(b + a))

for a in range(n_primes):
    s_a = str(primes[a])
    for b in range(a + 1, n_primes):
        s_b = str(primes[b])
        if check_prime_cocatenation(s_a, s_b):
            for c in range(b + 1, n_primes):
                s_c = str(primes[c])
                if check_prime_cocatenation(s_c, s_a) and check_prime_cocatenation(s_c, s_b):
                    for d in range(c + 1, n_primes):
                        s_d = str(primes[d])
                        if check_prime_cocatenation(s_d, s_a) and check_prime_cocatenation(s_d, s_b) and check_prime_cocatenation(s_d, s_c):
                            for e in range(d + 1, n_primes):
                                s_e = str(primes[e])
                                if check_prime_cocatenation(s_e, s_a) and check_prime_cocatenation(s_e, s_b) and check_prime_cocatenation(s_e, s_c) and check_prime_cocatenation(s_e, s_d):
                                    print("--", s_a, s_b, s_c, s_d, s_e)
                                    print("--", int(s_a) + int(s_b) + int(s_c) + int(s_d) + int(s_e))
                                    exit(0)