import sys
from collections import deque

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998_244_353
MOD = 10 ** 9 + 7
# DIR4 = ((-1, 0), (0, 1), (1, 0), (0, -1)) #URDL
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

def solve() -> None:
    n, m, q = mint()
    g = [[] for _ in range(n)]
    deg = [0] * n
    for _ in range(m):
        u, v = mint()
        g[u - 1].append(v - 1)
        deg[v - 1] += 1
    cnt = [0] * n
    for _ in range(q):
        cnt[sint() - 1] += 1
    
    q = deque(list(i for i, v in enumerate(deg) if v == 0))
    while q:
        u = q.popleft()
        for v in g[u]:
            cnt[v] = (cnt[v] + cnt[u]) % MOD
            deg[v] -= 1
            if deg[v] == 0:
                q.append(v)
    print(sum(cnt) % MOD)
    print(*cnt)


solve()