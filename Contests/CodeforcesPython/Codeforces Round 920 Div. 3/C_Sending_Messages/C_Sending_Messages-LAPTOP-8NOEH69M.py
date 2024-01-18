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
    n, f, a, b = mint()
    nums = ints()
    pre = 0
    for x in nums:
        f = max(f - (x - pre) * a, f - b)
        if f <= 0:
            print("NO")
            return
        pre = x
    print("YES")

for _ in range(int(input())):
    solve()