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
    n = sint()
    nums = [1e7] + ints()

    stmn = []
    stmx = []

    ans = valid = 0
    end = [None] * (n + 1)

    for r in range(n + 1):
        while stmn and nums[r] > nums[stmn[-1]]:
            if end[stmn[-1]]:
                i, dec_i = end[stmn[-1]]

                if dec_i < len(stmx) and stmx[dec_i] == i:
                    valid -= i - stmn[-1]

                    if dec_i == 0 or stmx[dec_i - 1] < stmn[-2]:
                        valid += i - stmn[-2]
                        end[stmn[-2]] = (i, dec_i)
                        end[i] = (stmn[-2], None)
                    else:
                        valid += i - stmx[dec_i - 1]
                        end[i] = (stmx[dec_i - 1], None)

            stmn.pop()

        while stmx and nums[r] < nums[stmx[-1]]:
            if end[stmx[-1]]:
                valid -= stmx[-1] - end[stmx[-1]][0]

            stmx.pop()
        
        stmn.append(r)
        stmx.append(r)
        
        end[r] = (r, len(stmx) - 1)

        ans += valid
    
    print(ans)

solve()