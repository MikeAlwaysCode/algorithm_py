import sys
from functools import reduce
from operator import xor

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
    l, r = mint()
    nums = ints()

    if (r - l + 1) & 1:
        print(reduce(xor, range(l, r + 1)) ^ reduce(xor, nums))
        return

    def f(l: int, r: int, s: set) -> int:
        if not l & 1 and r & 1:
            return f(l >> 1, r >> 1, set(v >> 1 for v in s)) << 1
        else:
            for v in s:
                if v ^ 1 not in s:
                    ok = True
                    ans = v
                    if l & 1: ans ^= l
                    else: ans ^= r
                    for x in s:
                        if (x ^ ans) < l or (x ^ ans) > r:
                            ok = False
                            break
                    if ok: return ans
        
    print(f(l, r, set(nums)))

for _ in range(int(input())):
    solve()
