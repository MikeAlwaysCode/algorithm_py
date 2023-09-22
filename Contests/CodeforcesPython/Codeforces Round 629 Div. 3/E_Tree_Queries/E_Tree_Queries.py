import sys

# import itertools
# import math
# import os
# import random
# from bisect import bisect, bisect_left
# from collections import *
# from functools import reduce
# from heapq import heapify, heappop, heappush
# from io import BytesIO, IOBase
# from string import *

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

# region dfsconvert
from types import GeneratorType
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
# endregion dfsconvert

# MOD = 998244353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def solve() -> None:
    n, m = mint()
    g = [[] for _ in range(n)]
    tin = [0] * n
    tout = [0] * n
    depth = [0] * n
    parent = [-1] * n
    for _ in range(n - 1):
        u, v = mint()
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)
    
    t = 0
    @bootstrap
    def dfs(x: int, p: int, d: int):
        parent[x] = p
        depth[x] = d
        nonlocal t
        t += 1
        tin[x] = t
        for y in g[x]:
            if y == p: continue
            yield dfs(y, x, d + 1)
        t += 1
        tout[x] = t
        yield

    dfs(0, -1, 0)
    
    for _ in range(m):
        q = ints()
        u = q[1] - 1
        for v in q[2:]:
            v -= 1
            if depth[u] < depth[v]:
                u = v
        for i in range(1, len(q)):
            q[i] -= 1
            if q[i] == u: continue
            if parent[q[i]] != -1:
                q[i] = parent[q[i]]
        
        check = True
        for v in q[1:]:
            if tin[v] > tin[u] or tout[v] < tout[u]:
                check = False
                break
        
        print("YES" if check else "NO")

solve()
