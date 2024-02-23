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

t2i = {'C':0,
       'P':1,
       'S':2}

def solve() -> None:
    n = sint()
    parent = [-1] + ints()
    t = input()
    dp = [[0] * 3 for _ in range(n)]
    deg = [0] * n
    for i in range(n):
        if parent[i] != -1:
            parent[i] -= 1
            deg[parent[i]] += 1
        k = t2i[t[i]]
        if k:
            dp[i][0] = dp[i][k ^ 3] = math.inf
    
    q = deque([i for i in range(n) if deg[i] == 0])
    while q:
        u = q.popleft()
        p = parent[u]
        k = t2i[t[p]]
        if k:
            dp[p][k] += min(dp[u][0], dp[u][k], dp[u][k ^ 3] + 1)
        else:
            dp[p][0] += min(dp[u][0], dp[u][1] + 1, dp[u][2] + 1)
            dp[p][1] += min(dp[u][0], dp[u][1], dp[u][2] + 1)
            dp[p][2] += min(dp[u][0], dp[u][1] + 1, dp[u][2])

        deg[p] -= 1
        if p and deg[p] == 0:
            q.append(p)
    
    print(min(dp[0]))



for _ in range(int(input())):
    solve()
