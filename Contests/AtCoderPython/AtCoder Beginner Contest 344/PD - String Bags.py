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
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))


def solve() -> None:
    t = input()
    m = len(t)
    dp = [math.inf] * (m + 1)
    dp[0] = 0
    n = sint()
    for _ in range(n):
        s = input().split()
        ndp = dp[:]
        for w in s[1:]:
            l = len(w)
            for i in range(m - l + 1):
                if dp[i] != math.inf and t[i:i + l] == w:
                    ndp[i + l] = min(ndp[i + l], dp[i] + 1)
        dp = ndp

    print(-1 if dp[-1] == math.inf else dp[-1])


solve()
