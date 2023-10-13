import sys
import math
from heapq import heapify, heappop, heappush

# import os
# import random
# from bisect import bisect, bisect_left
# from collections import *
# from functools import reduce
# from itertools import *
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

# MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR4 = ((-1, 0), (0, 1), (1, 0), (0, -1)) #URDL
DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

def solve() -> None:
    sx, sy, tx, ty = mint()
    d = dict()
    for _ in range(sint()):
        r, c1, c2 = mint()
        for c in range(c1, c2 + 1):
            d[(r, c)] = math.inf
    
    d[(sx, sy)] = 0
    h = [(0, sx, sy)]
    while h:
        dis, x, y = heappop(h)
        if dis > d[(x, y)]:
            continue
        for dx, dy in DIR8:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in d or dis + 1 >= d[(nx, ny)]:
                continue
            d[(nx, ny)] = dis + 1
            if nx == tx and ny == ty:
                break
            heappush(h, (d[(nx, ny)], nx, ny))
        if d[(tx, ty)] != math.inf: break
    print(-1 if d[(tx, ty)] == math.inf else d[(tx, ty)])

solve()