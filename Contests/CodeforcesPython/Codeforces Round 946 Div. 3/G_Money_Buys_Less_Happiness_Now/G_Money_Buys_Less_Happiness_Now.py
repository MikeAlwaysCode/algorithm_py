import sys
from heapq import *

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
    n, x = mint()
    nums = ints()
    ans = s = 0
    h = []
    for a in nums:
        if s >= a:
            ans += 1
            s -= a
            heappush(h, -a)
        elif h and h[0] + a < 0:
            s -= a + heapreplace(h, -a)
        s += x
    print(ans)


for _ in range(int(input())):
    solve()
