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
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))


def solve() -> None:
    n = sint()
    nums = ints()
    g = [-1] * n
    deg = [0] * n
    for x, y in enumerate(nums):
        g[x] = y - 1
        deg[y - 1] += 1
    seen = [False] * n
    sz = [1] * n
    q = deque(list(i for i in range(n) if deg[i] == 0))
    ans = 0
    while q:
        u = q.popleft()
        seen[u] = True
        ans += sz[u]
        sz[g[u]] += sz[u]
        deg[g[u]] -= 1
        if deg[g[u]] == 0:
            q.append(g[u])
    for i in range(n):
        if seen[i]:
            continue
        cnt = v = 0
        x = i
        while not seen[x]:
            cnt += sz[x]
            v += 1
            seen[x] = True
            x = g[x]
        ans += cnt * v
    print(ans)


solve()
