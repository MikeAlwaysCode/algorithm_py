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
    n = sint()
    l = ints()
    r = ints()
    c = ints()
    l.sort()
    r.sort()
    seg = []
    pl, pr = [], []
    for a, b in zip(l, r):
        while pr and a > pr[0]:
            seg.append(heappop(pr) - pl[-1])
            pl.pop()
        pl.append(a)
        heappush(pr, b)
    while pr:
        seg.append(heappop(pr) - pl[-1])
        pl.pop()
    seg.sort()
    c.sort(reverse=True)
    ans = sum(s * x for s, x in zip(seg, c))
    print(ans)


for _ in range(int(input())):
    solve()
