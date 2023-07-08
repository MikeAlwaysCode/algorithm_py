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
DIR = ((1, 0), (0, 1), (-1, 0), (0, -1))

def solve() -> None:
    n = sint()
    g = []
    for _ in range(n):
        g.append(list(input()))
    
    c = g[1][0]
    x, y = 1, 0
    d = 0
    while x != 0 or y != 0:
        nx, ny = x + DIR[d][0], y + DIR[d][1]
        if 0 <= nx < n and 0 <= ny < n:
            g[x][y] = g[nx][ny]
            x, y = nx, ny
        else:
            d = (d + 1) % 4
    g[0][0] = c 
    
    for row in g:
        print("".join(row))

solve()