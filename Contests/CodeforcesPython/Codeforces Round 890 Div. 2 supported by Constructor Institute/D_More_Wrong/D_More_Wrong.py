import sys

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

# region interactive
def printQry(l, r) -> int:
    if l == r: return 0
    sa = str(l)
    sb = str(r)
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

# MOD = 998244353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def solve() -> None:
    n = sint()

    # Divide and conquer 分治
    def dc(l: int, r: int) -> int:
        if l == r: return l
        mid = l + r >> 1
        resl, resr = dc(l, mid), dc(mid + 1, r)
        invl, invr = printQry(resl, resr - 1), printQry(resl, resr)
        if invl == invr:
            return resr
        else:
            return resl
    
    ans = dc(1, n)
    printAns(ans)

for _ in range(int(input())):
    solve()