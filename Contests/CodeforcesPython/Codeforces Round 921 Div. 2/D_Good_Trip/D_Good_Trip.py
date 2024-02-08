import sys

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998_244_353
MOD = 10 ** 9 + 7
# DIR4 = ((-1, 0), (0, 1), (1, 0), (0, -1)) #URDL
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

def solve() -> None:
    n, m, k = mint()
    p = 0
    for _ in range(m):
        a, b, f = mint()
        p = (p + f) % MOD
        
    q = n * (n - 1) // 2
    q_inv = pow(q, MOD - 2, MOD)
    ans = p * k % MOD * q_inv % MOD
    avg_inc = 0
    comb = 1
    unpick = (q - 1) * q_inv % MOD
    q1_inv = pow(q - 1, MOD - 2, MOD)
    unpick_k = pow(unpick, k, MOD)
    inv_k = 1
    for i in range(1, k + 1):
        s = i * (i - 1) // 2    # 0, 1, 2
        comb = comb * (k - i + 1) * pow(i, MOD - 2, MOD) % MOD
        inv_k = inv_k * q_inv % MOD
        if i == k:
            unpick_k = 1
        else:
            unpick_k = unpick_k * q1_inv * q % MOD
        # prob = comb * pow(q_inv, i, MOD) * pow(unpick, k - i, MOD)
        prob = comb * inv_k * unpick_k % MOD
        avg_inc = (avg_inc + s * prob) % MOD

    ans = (ans + (m * avg_inc) % MOD) % MOD
    '''
    ans = 0
    q0 = q = n * (n - 1) // 2
    ans = p * pow(q, MOD - 2, MOD) % MOD
    more = m
    for _ in range(k - 1):
        p = (p * q + more) % MOD
        q0 = q0 * q % MOD
        ans = (ans + p * pow(q0, MOD - 2, MOD)) % MOD
        more = more * q % MOD
    '''
    print(ans)


for _ in range(int(input())):
    solve()