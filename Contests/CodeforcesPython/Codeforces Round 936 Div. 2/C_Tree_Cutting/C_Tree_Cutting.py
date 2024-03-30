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
    n, k = mint()
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = mint()
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)
    
    parent = [-1] * n
    q = deque([0])
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in g[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            q.append(v)

    def check(x: int) -> bool:
        cnt = 0
        sz = [1] * n
        for u in order[::-1]:
            if sz[u] >= x:
                cnt += 1
            elif (p := parent[u]) != -1:
                sz[p] += sz[u]

        return cnt > k

    l, r = 1, n
    while l < r:
        mid = (l + r + 1) // 2
        if check(mid):
            l = mid
        else:
            r = mid - 1
    print(l)


for _ in range(int(input())):
    solve()
