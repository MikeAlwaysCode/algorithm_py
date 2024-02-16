import math
import sys
from collections import deque

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
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = mint()
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)
    
    vmask = [0] * n
    k = sint()
    for i in range(k):
        u, v = mint()
        u -= 1
        v -= 1
        vmask[u] |= 1 << i
        vmask[v] |= 1 << i
    
    parent = [-1] * n
    q = deque([(0, -1)])
    s = [0]
    while q:
        u, p = q.popleft()
        for v in g[u]:
            if v == p:
                continue
            s.append(v)
            parent[v] = u
            q.append((v, u))

    trans = []
    for u in s[::-1]:
        p = parent[u]
        if p != -1:
            vmask[p] ^= vmask[u]
        for v in g[u]:
            if v == p:
                continue
            # 被子节点抵消，需要一条到子节点的边
            if ~vmask[u] & vmask[v]:
                trans.append(vmask[v])
    
    dp = [math.inf] * (1 << k)
    dp[0] = 0
    for mask in range(1 << k):
        for s in trans:
            dp[mask | s] = min(dp[mask | s], dp[mask] + 1)
    print(dp[-1])


for _ in range(int(input())):
    solve()
