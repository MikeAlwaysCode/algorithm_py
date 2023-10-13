import sys

# import math
# import os
# import random
# from bisect import bisect, bisect_left
# from collections import *
# from functools import reduce
# from heapq import heapify, heappop, heappush
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

# region interactive
def printQry(a, b) -> int:
    sa = str(a)
    sb = str(b)
    print(f"? {sa} {sb}", flush = True)
    return sint()

def printAns(ans) -> None:
    s = str(ans)
    print(f"! {s}", flush = True)
# endregion interactive

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
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

def solve() -> None:
    n = sint()
    smax = printQry(1, n)
    if smax == 1:
        l, r = 2, n
    elif smax == n:
        l, r = 1, n - 1
    else:
        nmax = printQry(1, smax)
        if nmax == smax:
            l, r = 1, smax - 1
        else:
            l, r = smax + 1, n
            
    while l < r:
        if r < smax:
            mid = (l + r + 1) >> 1
            nmax = printQry(mid, smax)
            if nmax != smax:
                r = mid - 1
            else:
                l = mid
        else:
            mid = (l + r) >> 1
            nmax = printQry(smax, mid)
            if nmax != smax:
                l = mid + 1
            else:
                r = mid
    printAns(r)

solve()