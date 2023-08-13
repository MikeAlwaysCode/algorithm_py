import sys

# import math
# from bisect import *
# from collections import *
# from functools import *
# from heapq import *
# from itertools import *
# from random import *
# from string import *
# from types import GeneratorType

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

MOD = 998244353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def solve() -> None:
    n = sint()
    p = [0] * n

    fa = list(range(n))
    sz = [1] * n
    def find(x: int):
        cur = x
        while x != fa[x]:
            x = fa[x]
        while fa[cur] != x:
            fa[cur], cur = x, fa[cur]
        return x

    def union(fr: int, to: int):
        fr, to = find(fr), find(to)
        if fr < to: fr, to = to, fr
        sz[to] += sz[fr]
        fa[find(fr)] = find(to)


    edge = []
    dp = [[0] * 2 for _ in range(n)]
    for i in range(n - 1):
        u, v = mint()
        u -= 1
        v -= 1
        fu, fv = find(u), find(v)
        edge.append((fu, fv))

        tot = sz[fu] + sz[fv]
        dp[i][0], dp[i][1] = sz[fu] * pow(tot, MOD - 2, MOD) % MOD, sz[fv] * pow(tot, MOD - 2, MOD) % MOD
        union(fu, fv)

    for i in range(n - 2, -1, -1):
        u, v = edge[i]
        x, y = min(u, v), max(u, v)
        p[y] = (p[y] + p[x]) % MOD
        p[u] = (p[u] + dp[i][0]) % MOD
        p[v] = (p[v] + dp[i][1]) % MOD
    
    print(*p)

solve()