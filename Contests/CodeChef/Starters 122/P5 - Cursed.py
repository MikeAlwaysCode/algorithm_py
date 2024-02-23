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
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = mint()
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)
    
    parent = [-1] * n
    depth = [0] * n
    q = deque([(0, -1)])
    s = []
    while q:
        u, p = q.popleft()
        for v in g[u]:
            if v == p:
                continue
            parent[v] = u
            depth[v] = depth[u] + 1
            q.append((v, u))
            s.append(v)
    
    dp = [[0] * 2 for _ in range(n)]
    dp[0][0] = nums[0]
    for u in s[::-1]:
        dp[u][0] += nums[u] - depth[u]
        # dp[u][0] = max(dp[u][0], 0)
        dp[parent[u]][0] += max(dp[u][0], 0)

        dp[u][1] += nums[u] - depth[u] + 1
        # dp[u][1] = max(dp[u][1], 0)
        dp[parent[u]][1] += max(dp[u][1], 0)

    ans = [dp[0][0]] * (n - 1)
    # for i in range(1, n):
    #     ans[i - 1] = max(ans[i - 1], dp[0][0] - max(0, dp[i][0]) + dp[i][1])
    
    q = deque([(0, 0)])
    while q:
        u, pres = q.popleft()
        if u:
            ans[u - 1] = max(ans[u - 1], dp[u][1] + pres)
        for v in g[u]:
            if v == parent[u]:
                continue
            q.append((v, pres + dp[u][0] - max(0, dp[v][0])))
            
    print(*ans)


for _ in range(sint()):
    solve()
