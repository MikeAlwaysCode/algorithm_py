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
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def solve() -> None:
    n = sint()
    g = [[] for _ in range(n)]
    deg = [0] * n
    sz = [1] * n
    for i in range(1, n):
        u, v = mint()
        u -= 1
        v -= 1
        g[u].append((v, i))
        g[v].append((u, i))
        deg[u] += 1
        deg[v] += 1
    ans = set()
    q = deque([i for i in range(n) if deg[i] == 1])
    while q:
        u = q.popleft()
        for v, i in g[u]:
            if sz[v] == 0: continue
            if sz[u] == 3:
                ans.add(i)
            else:
                sz[v] += sz[u]
                sz[u] = 0
            deg[v] -= 1
            if deg[v] == 1:
                q.append(v)
        if sz[u] != 0 and sz[u] != 3:
            print(-1)
            return
        sz[u] = 0

    print(len(ans))
    print(*ans)

for _ in range(int(input())):
    solve()