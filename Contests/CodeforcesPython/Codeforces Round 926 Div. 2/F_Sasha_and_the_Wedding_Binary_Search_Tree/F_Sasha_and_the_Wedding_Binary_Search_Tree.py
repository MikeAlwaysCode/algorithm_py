import sys

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR4 = ((-1, 0), (0, 1), (1, 0), (0, -1)) #URDL
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

def solve() -> None:
    n, C = mint()
    L, R = [-1] * (n + 1), [-1] * (n + 1)
    val = [-1] * (n + 1)
    for i in range(1, n + 1):
        L[i], R[i], val[i] = mint()
    
    s = [1]
    stk = []
    node = 1
    while stk or node != -1:
        while node != -1:
            stk.append(node)
            node = L[node]
        node = stk.pop()
        s.append(val[node])
        node = R[node]
    s.append(C)
    
    def comb(n: int, m: int) -> int:
        res = inv = 1
        for i in range(1, m + 1):
            res = res * (n - i + 1) % MOD
            inv = inv * i % MOD
        return res * pow(inv, MOD - 2, MOD) % MOD
    
    ans, j = 1, 0
    for i in range(1, n + 2):
        if s[i] != -1:
            if i - j > 1:
                k = i - j - 1
                m = s[i] - s[j] + 1
                ans = ans * comb(k + m - 1, k) % MOD
            j = i
    print(ans)

for _ in range(int(input())):
    solve()
