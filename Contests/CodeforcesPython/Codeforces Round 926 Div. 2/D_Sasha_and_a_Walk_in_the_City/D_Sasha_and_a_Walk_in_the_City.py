import sys
from collections import deque

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

MOD = 998_244_353
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
    '''
    ans = n + 1
    child = [0] * n
    cnt = [0] * n
    for u in s[::-1]:
        p = parent[u]
        ans = (ans + child[u]) % MOD
        if p != -1:
            ans = (ans + cnt[p] * (cnt[u] + 1) % MOD + cnt[u]) % MOD
            cnt[p] = (cnt[p] + (cnt[p] + 1) * (cnt[u] + 1) % MOD) % MOD
            child[p] = (child[p] + 1) % MOD
    # print(cnt)
    print(ans)
    '''
    dp = [1] * n
    for u in s[::-1]:
        p = parent[u]
        if p != -1:
            dp[p] = dp[p] * (dp[u] + 1) % MOD
    
    print((sum(dp) + 1) % MOD)


for _ in range(int(input())):
    solve()
