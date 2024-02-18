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
    n, w = mint()
    dp = [math.inf] * (10 ** 5 + 1)
    dp[0] = 0
    for _ in range(n):
        a, v = mint()
        for i in range(10 ** 5, v - 1, -1):
            dp[i] = min(dp[i], dp[i - v] + a)
    
    for i in range(10 ** 5, 0, -1):
        if dp[i] <= w:
            print(i)
            return
    print(0)


solve()
