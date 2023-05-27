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
    n, m = mint()
    edges = []
    for _ in range(m):
        u, v, c = mint()
        edges.append((u, v, c))

    cnt = Counter()
    fa = list(range(n + 1))
    def find(x: int):
        cur = x
        while x != fa[x]:
            x = fa[x]
        while fa[cur] != x:
            tmp = fa[cur]
            fa[cur] = x
            cur = tmp
        return x

    edges.append((n, n, m + 1))
    edges.sort(key = lambda x: x[2])
    prec = 0
    vs = set()
    for u, v, c in edges:
        if c != prec:
            # 计数 & 重置并查集
            vl = sorted(vs)
            for i, x in enumerate(vl):
                for j in range(i + 1, len(vl)):
                    y = vl[j]
                    if find(x) == find(y):
                        cnt[(x, y)] += 1
                fa[x] = x

            prec = c
            vs.clear()

        fu = find(u)
        fv = find(v)
        fa[fv] = fu
        vs.add(u)
        vs.add(v)

    q = sint()
    for _ in range(q):
        u, v = mint()
        if u > v: u, v = v, u
        print(cnt[(u, v)])

# for _ in range(int(input())):
solve()