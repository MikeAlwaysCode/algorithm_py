import math
import sys

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR4 = ((-1, 0), (0, 1), (1, 0), (0, -1)) #URDL
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))


def solve() -> None:
    n = sint()
    A = ints()
    B = ints()
    ans = math.inf
    t = tot = 0
    s = sum(max(a, b) for a, b in zip(A, B))
    dp = [False] * (s + 1)
    dp[0] = True
    for a, b in zip(A, B):
        t += (n - 2) * (a * a + b * b)
        tot += a + b
        for i in range(s, -1, -1):
            if dp[i]:
                if i + a <= s:
                    dp[i + a] = True
                if i + b <= s:
                    dp[i + b] = True
                dp[i] = False
    for i in range(s + 1):
        if dp[i]:
            ans = min(ans, t + i * i + (tot - i) * (tot - i))
    print(ans)

for _ in range(int(input())):
    solve()
