import sys
from collections import *

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

# # region dfsconvert
# from types import GeneratorType
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
    deg = [0] * n
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = mint()
        u -= 1
        v -= 1
        deg[u] += 1
        deg[v] += 1
        g[u].append(v)
        g[v].append(u)

    if n == 2:
        print(2, 2)
        print(1, 1)
        return

    # f: 当前节点需要计数时子树有效节点数和w和
    f1 = [[0] * 2 for _ in range(n)]
    # g: 当前节点不计数时子树有效节点数和w和
    f2 = [[0] * 2 for _ in range(n)]
    # BFS 构造序列和父子关系
    s = []
    parent = [-1] * n
    q = deque([(0, -1)])
    while q:
        x, p = q.popleft()
        f1[x][0], f1[x][1] = 1, deg[x]
        for y in g[x]:
            if y == p: continue
            parent[y] = x
            s.append(y)
            q.append((y, x))
    
    for x in s[::-1]:
        p = parent[x]
        # 父节点有效时，子节点必定无效
        f1[p][0] += f2[x][0]
        f1[p][1] += f2[x][1]

        # 父节点无效时，子节点选择最优的状态转移
        if f2[x][0] > f1[x][0] or (f2[x][0] == f1[x][0] and f2[x][1] <= f1[x][1]):
            f2[p][0] += f2[x][0]
            f2[p][1] += f2[x][1]
        else:
            f2[p][0] += f1[x][0]
            f2[p][1] += f1[x][1]
    
    w = [0] * n
    q = deque([(0, -1, f2[0][0] > f1[0][0] or (f2[0][0] == f1[0][0] and f2[0][1] <= f1[0][1]))])
    while q:
        x, p, t = q.popleft()
        if t:   # 无效节点
            w[x] = 1
        else:   # 有效节点
            w[x] = deg[x]
        for y in g[x]:
            if y == p: continue
            # 父节点有效时，子节点务必无效，父节点无效时，子节点根据最优情况判断
            if not t or f2[y][0] > f1[y][0] or (f2[y][0] == f1[y][0] and f2[y][1] <= f1[y][1]):
                q.append((y, x, True))
            else:
                q.append((y, x, False))

    print(max(f1[0][0], f2[0][0]), sum(w))
    print(*w)


solve()