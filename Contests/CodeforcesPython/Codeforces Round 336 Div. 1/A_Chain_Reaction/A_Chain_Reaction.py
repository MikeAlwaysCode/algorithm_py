import sys
from bisect import bisect_left

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
    pos = [(-2 * 10 ** 6, 0)]
    for i in range(n):
        pos.append(tuple(mint()))
    pos.sort()
    dp = [0] * (n + 1)
    ans = n - 1
    for i in range(n):
        j = bisect_left(pos, (pos[i + 1][0] - pos[i + 1][1], 0))
        dp[i + 1] = dp[j - 1] + 1
        ans = min(ans, n - dp[i + 1])
    # print(dp)
    print(ans)


solve()
