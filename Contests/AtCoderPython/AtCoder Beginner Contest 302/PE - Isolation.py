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
    n, q = mint()
    cnt = n
    edge = [set() for _ in range(n)]
    
    for _ in range(q):
        qry = ints()
        if qry[0] == 1:
            u, v = qry[1] - 1, qry[2] - 1
            edge[u].add(v)
            edge[v].add(u)
            if len(edge[u]) == 1:
                cnt -= 1
            if len(edge[v]) == 1:
                cnt -= 1
            print(cnt)
        else:
            u = qry[1] - 1
            for v in edge[u]:
                edge[v].remove(u)
                if not edge[v]: cnt += 1
            if edge[u]:
                cnt += 1
                edge[u].clear()
            print(cnt)

solve()