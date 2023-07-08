import math
import sys
from heapq import heapify, heappop, heappush

# import itertools
# import os
# import random
# from bisect import bisect, bisect_left
# from collections import *
# from functools import reduce
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
    n, m = mint()
    o = int(input(), base = 2)
    ans = math.inf
    dist = [math.inf] * (1 << n)
    mask = (1 << n) - 1
    med = []
    valid = False
    for _ in range(m):
        d = sint()
        x = int(input(), base = 2)
        y = int(input(), base = 2)
        x ^= mask
        if y == 0:
            valid = True
        
        med.append((d, x, y))

    if o == 0:
        print(0)
        return
    
    if not valid:
        print(-1)
        return

    dist[o] = 0
    h = [(0, o)]
    while h:
        d, x = heappop(h)
        for nd, nx, ny in med:
            to = x & nx | ny
            if d + nd < dist[to]:
                dist[to] = d + nd
                heappush(h, (dist[to], to))
            
    print(-1 if dist[0] == math.inf else dist[0])

for _ in range(int(input())):
    solve()