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
    n, d = mint()
    point = []
    for _ in range(n):
        x, y = mint()
        point.append((x, y))
    
    fa = list(range(n))
    def find(x: int) -> int:
        cur = x
        while x != fa[x]:
            x = fa[x]
        while fa[cur] != x:
            tmp = fa[cur]
            fa[cur] = x
            cur = tmp
        return x
    
    d *= d
    for i in range(n):
        xi, yi = point[i]
        fi = find(i)
        for j in range(i + 1, n):
            xj, yj = point[j]
            fj = find(j)
            if fj == fi: continue
            if (xi - xj) * (xi - xj) + (yi - yj) * (yi - yj) <= d:
                fa[fj] = fi
    
    f0 = find(0)
    for i in range(n):
        print("Yes" if f0 == find(i) else "No")

solve()