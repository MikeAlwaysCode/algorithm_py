import sys
from collections import Counter

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
    ans = 0
    cntx, cnty, cnt = Counter(), Counter(), Counter()
    for _ in range(n):
        x, y = mint()
        # 1528 ms
        # ans += cntx[x] + cnty[y] - cnt[(x, y)]
        cntx[x] += 1
        cnty[y] += 1
        cnt[(x, y)] += 1
    for c in cntx.values():
        ans += c * (c - 1) // 2
    for c in cnty.values():
        ans += c * (c - 1) // 2
    for c in cnt.values():
        ans -= c * (c - 1) // 2
    print(ans)


solve()
