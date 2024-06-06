import sys
from collections import defaultdict
from random import getrandbits

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
    n, m, k = mint()
    h = getrandbits(30)
    rs = set()
    row = defaultdict(list)
    for i in range(k):
        r, c = mint()
        rs.add(r ^ h)
        row[r ^ h].append((c, i))
    s = 0
    ans = [0] * k
    rs = sorted(r ^ h for r in rs)
    l = len(rs)
    suff = [m + 1] * (l + 1)
    p = n

    stk = []
    up = [0] * l
    gt = [m + 1] * l
    for i in range(l - 1, -1, -1):
        row[rs[i] ^ h].sort()
        cc = row[rs[i] ^ h][0][0]
        suff[i] = cc
        suff[i] = min(suff[i], suff[i + 1])
        s += (suff[i + 1] - 1) * (p - rs[i])
        p = rs[i]

    for i in range(l):
        cc = row[rs[i] ^ h][0][0]
        while stk and row[stk[-1] ^ h][0][0] > cc:
            gt[i] = min(gt[i], row[stk.pop() ^ h][0][0])
        up[i] = 0 if not stk else stk[-1]
        stk.append(rs[i])
    # print(gt)
    # print(up)
    s += (suff[0] - 1) * p

    for i in range(l):
        mn = suff[i + 1]
        if len(row[rs[i] ^ h]) > 1:
            mn = min(mn, row[rs[i] ^ h][1][0])
        p = rs[i] if i == 0 else rs[i] - rs[i - 1]
        p2 = 0 if i == 0 else rs[i - 1] - up[i]
        ans[row[rs[i] ^ h][0][1]] = (mn - suff[i]) * p + max(0, (min(mn, gt[i]) - suff[i]) * p2)


    print(s)
    print(*ans)


for _ in range(int(input())):
    solve()
