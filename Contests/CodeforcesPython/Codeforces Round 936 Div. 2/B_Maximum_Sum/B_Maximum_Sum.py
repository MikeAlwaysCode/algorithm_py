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
    n, k = mint()
    nums = ints()
    s = sum(nums)
    mx = cur = 0
    for x in nums:
        cur = max(cur + x, x)
        mx = max(mx, cur)
    if mx:
        s += mx * (pow(2, k, MOD) - 1) % MOD
    print(s % MOD)

for _ in range(int(input())):
    solve()
