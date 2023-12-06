import sys
from bisect import *
from collections import *

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998_244_353
# MOD = 10 ** 9 + 7
DIR4 = ((-1, 0), (0, 1), (1, 0), (0, -1)) #URDL
S2D = "LURD"
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

def solve() -> None:
    n, q = mint()
    s = input()
    p2r = defaultdict(list)
    p2r[(0, 0)].append(0)
    pos = [(0, 0)]
    x, y = 0, 0
    for i, c in enumerate(s, 1):
        j = S2D.index(c)
        x += DIR4[j][0]
        y += DIR4[j][1]
        pos.append((x, y))
        p2r[(x, y)].append(i)
    p2l = defaultdict(list)
    p2l[(0, 0)].append(0)
    pos2 = [(0, 0)]
    x, y = 0, 0
    for i in range(n - 1, -1, -1):
        j = S2D.index(s[i])
        x += DIR4[j][0]
        y += DIR4[j][1]
        pos2.append((x, y))
        p2l[(x, y)].append(n - i)

    for _ in range(q):
        x, y, l, r = mint()
        if p2r[(x, y)]:
            j = bisect_left(p2r[(x, y)], l)
            if j:
                print("YES")
                continue
            j = bisect(p2r[(x, y)], r)
            if j < len(p2r[(x, y)]):
                print("YES")
                continue
        x0, y0 = pos[l - 1]
        x -= x0
        y -= y0
        l, r = n - r + 1, n - l + 1
        x += pos2[l - 1][0]
        y += pos2[l - 1][1]
        if p2l[(x, y)]:
            j = bisect_left(p2l[(x, y)], l)
            if j < len(p2l[(x, y)]) and p2l[(x, y)][j] <= r:
                print("YES")
                continue
            j = bisect(p2l[(x, y)], r)
            if j and p2l[(x, y)][j - 1] >= l:
                print("YES")
                continue
        print("NO")
    

solve()