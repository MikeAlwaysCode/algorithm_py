import sys
from collections import Counter, deque

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
    col = ints()
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = mint()
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)
    
    s = [Counter() for _ in range(n)]
    parent = [-1] * n
    q = deque([0])
    order = []
    while q:
        u = q.popleft()
        s[u][col[u]] = 1
        for v in g[u]:
            if v == parent[u]:
                continue
            order.append(v)
            parent[v] = u
            q.append(v)
    
    ans = 0
    for u in order[::-1]:
        p = parent[u]
        if len(s[p]) < len(s[u]):
            s[p], s[u] = s[u], s[p]
        for k, v in s[u].items():
            ans += v * s[p][k]
            s[p][k] += v
        s[p][col[p]] = 1
    print(ans)


for _ in range(int(input())):
    solve()
