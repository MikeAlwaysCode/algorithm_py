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
    n, m = mint()
    nums = ints()
    dp = [False] * n
    dp[0] = True
    for x in nums:
        ndp = [False] * n
        for i in range(n):
            ndp[i] = dp[(i - x) % n] | dp[(i + x) % n]
        dp = ndp
    print("YES" if dp[0] else "NO")


solve()
