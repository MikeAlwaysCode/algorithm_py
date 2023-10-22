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
    n, m = mint()
    seg = []
    for _ in range(n):
        l, r = mint()
        if l != 1 or r != m:
            seg.append((l, r))
    
    if not seg:
        print(0)
        return
    
    a1 = am = ans = 0
    seg.sort()
    h = []
    for l, r in seg:
        if l == 1:
            a1 += 1
        if r == m:
            am += 1
        while h and h[0][0] < l:
            pr, pl = heappop(h)
            if pl == 1:
                a1 -= 1
        heappush(h, (r, l))
        ans = max(ans, len(h) - min(a1, am))
    print(ans)

for _ in range(int(input())):
    solve()