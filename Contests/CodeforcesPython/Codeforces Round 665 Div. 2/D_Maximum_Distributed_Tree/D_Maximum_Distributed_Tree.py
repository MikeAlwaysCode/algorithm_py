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
# print = lambda d: sys.stdout.write(str(d) + "\n")
# endregion fastio

# # region interactive
# def printQry(a, b) -> None:
#     sa = str(a)
#     sb = str(b)
#     print(f"? {sa} {sb}", flush = True)

# def printAns(ans) -> None:
#     s = str(ans)
#     print(f"! {s}", flush = True)
# # endregion interactive

# # region dfsconvert
# def bootstrap(f, stack=[]):
#     def wrappedfunc(*args, **kwargs):
#         if stack:
#             return f(*args, **kwargs)
#         else:
#             to = f(*args, **kwargs)
#             while True:
#                 if type(to) is GeneratorType:
#                     stack.append(to)
#                     to = next(to)
#                 else:
#                     stack.pop()
#                     if not stack:
#                         break
#                     to = stack[-1].send(to)
#             return to
#     return wrappedfunc
# # endregion dfsconvert

# MOD = 998244353
MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def solve() -> None:
    n = sint()
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

    m = sint()
    p = ints()
    
    cnt = [1] * n
    v = []
    # if k == 2:
    q = deque([i for i in range(n) if deg[i] == 1])
    while q:
        x = q.popleft()
        if cnt[x] < n: v.append(cnt[x] * (n - cnt[x]))
        for y in g[x]:
            if deg[y] < 1: continue
            cnt[y] += cnt[x]
            deg[y] -= 1
            if deg[y] == 1:
                q.append(y)
    
    # print(v)
    v.sort(reverse = True)
    p.sort(reverse = True)
    ans = i = j = 0
    while i <= m - n:
        # ans = (ans + p[i] * v[0]) % MOD
        p[i + 1] = p[i + 1] * p[i] % MOD
        i += 1
    while i < m and j < n - 1:
        ans = (ans + p[i] * v[j]) % MOD
        i += 1
        j += 1
    while j < n - 1:
        ans = (ans + v[j]) % MOD
        j += 1
    print(ans)

for _ in range(int(input())):
    solve()