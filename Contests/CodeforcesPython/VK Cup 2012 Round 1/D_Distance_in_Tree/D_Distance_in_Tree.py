import math
import sys
from bisect import *
from collections import *
from functools import *
from heapq import *
from itertools import *
from random import *
from string import *
from types import GeneratorType

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# print = lambda d: sys.stdout.write(str(d) + " ")
# endregion fastio

# MOD = 998244353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

# # region dfsconvert
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc
# # endregion dfsconvert

def solve() -> None:
    n, k = mint()
    g = [[] for _ in range(n)]
    deg = [0] * n
    for _ in range(n - 1):
        u, v = mint()
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)
        deg[u] += 1
        deg[v] += 1

    dp = [[0] * (k + 1) for _ in range(n)]
    ans = 0

    # DFS
    @bootstrap
    def dfs(u: int, f: int) -> None:
        dp[u][0] = 1
        for v in g[u]:
            if v == f: continue
            yield dfs(v, u)
            for i in range(k):
                dp[u][i + 1] += dp[v][i]
                
        nonlocal ans
        ans += dp[u][k]
        cnt = 0
        for v in g[u]:
            if v == f: continue
            for i in range(1, k):
                cnt += dp[v][i - 1] * (dp[u][k - i] - dp[v][k - i - 1])
        ans += cnt // 2
        yield

    dfs(0, -1)

    '''
    # BFS -> Order: 1340 ms
    parent = [-1] * n
    order = [0]
    stack = [0]
    while stack:
        u = stack.pop()
        for v in g[u]:
            if v == parent[u]: continue
            parent[v] = u
            order.append(v)
            stack.append(v)
    
    for u in order[::-1]:
        dp[u][0] = 1
        for v in g[u]:
            if v == parent[u]: continue
            for i in range(k):
                dp[u][i + 1] += dp[v][i]
        
        ans += dp[u][k]
        cnt = 0
        for v in g[u]:
            if v == parent[u]: continue
            for i in range(1, k):
                cnt += dp[v][i - 1] * (dp[u][k - i] - dp[v][k - i - 1])
        ans += cnt // 2
    '''

    # print(dp)
    print(ans)

# for _ in range(int(input())):
solve()

# # region interactive
# def printQry(a, b) -> None:
#     sa = str(a)
#     sb = str(b)
#     print(f"? {sa} {sb}", flush = True)

# def printAns(ans) -> None:
#     s = str(ans)
#     print(f"! {s}", flush = True)
# # endregion interactive