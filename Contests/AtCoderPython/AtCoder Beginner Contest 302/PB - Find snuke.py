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
    h, w = mint()
    g = []
    for _ in range(h):
        g.append(list(input()))
    # print(g)
    t = "snuke"
    DIR = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    for i in range(h):
        for j in range(w):
            if g[i][j] != t[0]: continue
            
            for dr, dc in DIR:
                mi, mj = i + 4 * dr, j + 4 * dc
                if mi < 0 or mi >= h or mj < 0 or mj >= w: continue
                
                chk = True
                for k in range(1, 5):
                    if g[i + k * dr][j + k * dc] != t[k]:
                        chk = False
                        break
                
                if chk:
                    for k in range(5):
                        print(i + k * dr + 1, j + k * dc + 1)
                    return

solve()