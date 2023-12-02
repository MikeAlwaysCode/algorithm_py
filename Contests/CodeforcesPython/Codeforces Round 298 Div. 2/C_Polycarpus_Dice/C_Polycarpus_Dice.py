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
    n, t = mint()
    nums = ints()
    s = t - sum(nums)
    t -= n - 1
    ans = [0] * n
    for i, x in enumerate(nums):
        l = max(1, s + x)
        r = min(x, t)
        ans[i] = max(0, x - r + l - 1)
    print(*ans)

solve()