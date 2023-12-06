import sys
from collections import *

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
    s = list(map(int, input()))
    to = ints()
    deg = [0] * n
    for i, a in enumerate(to):
        deg[a - 1] += 1
    ans = []
    q = deque([i for i in range(n) if deg[i] == 0])
    while q:
        u = q.popleft()
        v = to[u]
        if s[u] == 1:
            ans.append(u)
            s[v] ^= 1
        deg[v] -= 1
        if deg[v] == 0:
            q.append(v)
    for i, d in enumerate(deg):
        if d == 0:
            continue
        ring = [i]
        p = []
        if s[i] == 1:
            p.append(0)
        v = to[i]
        while v != i:
            deg[v] = 0
            if s[v] == 1:
                p.append(len(ring))
            ring.append(v)
            v = to[v]
        if not p:
            continue
        if len(p) & 1:
            print(-1)
            return
        cnt = 0
        for i in range(1, len(p), 2):
            cnt += p[i] - p[i - 1]
        idx = p[0]
        if cnt > len(ring) - cnt:
            idx = p[1]



for _ in range(int(input())):
    solve()