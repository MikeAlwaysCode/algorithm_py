import sys
from heapq import *

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998244353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

def solve() -> None:
    n = sint()
    p = []
    time = set()
    for _ in range(n):
        p.append(tuple(mint()))
        time.add(p[-1][0])
    p.sort()
    ans = cur = j = 0
    h = []
    for t in sorted(time):
        while cur < t and h:
            d = heappop(h)
            if d >= cur:
                ans += 1
                cur += 1
        cur = t
        while j < n and p[j][0] <= t:
            heappush(h, (t + p[j][1]))
            j += 1
    while h:
        d = heappop(h)
        if d >= cur:
            ans += 1
            cur += 1
    print(ans)

solve()