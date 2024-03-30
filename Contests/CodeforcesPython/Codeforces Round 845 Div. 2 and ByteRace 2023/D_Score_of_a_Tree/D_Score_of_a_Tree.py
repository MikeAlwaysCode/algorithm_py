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
    n = sint()
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = mint()
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)
    p = [-1] * n
    q = deque([0])
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in g[u]:
            if v == p[u]:
                continue
            p[v] = u
            q.append(v)
    cnt = [0] * n
    ans = n
    for u in order[::-1]:
        ans += cnt[u]
        if p[u] != -1:
            cnt[p[u]] = max(cnt[p[u]], cnt[u] + 1)
    ans = ans * pow(2, n - 1, MOD) % MOD
    print(ans)


for _ in range(int(input())):
    solve()
