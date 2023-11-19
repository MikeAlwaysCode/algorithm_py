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
    nums = ints()

    ans = 0
    for k in range(1, n):
        if n % k:
            continue

        cur = 0
        mx, mn = 0, math.inf

        for i, x in enumerate(nums, 1):
            cur += x
            if i % k == 0:
                mx = max(mx, cur)
                mn = min(mn, cur)
                cur = 0
            
        ans = max(ans, mx - mn)
    print(ans)

for _ in range(int(input())):
    solve()