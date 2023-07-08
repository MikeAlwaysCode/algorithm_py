import sys
from functools import cache

# import itertools
# import math
# import os
# import random
# from bisect import bisect, bisect_left
# from collections import *
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
    s = input()
    t = input()

    # @cache
    # def f(s1: str, s2: str) -> bool:
    #     n = len(s1)
    #     if n & 1:
    #         return s1 == s2
        
    #     return s1 == s2 or f(s1[:n//2], s2[:n//2]) and f(s1[n//2:], s2[n//2:]) or (f(s1[:n//2], s2[n//2:]) and f(s1[n//2:], s2[:n//2]))
    # print("YES" if f(s, t) else "NO")

    def split_sort(s: str):
        n = len(s)
        if n & 1:
            return s
        a, b = split_sort(s[:n // 2]), split_sort(s[n // 2:])
 
        return a + b if a < b else b + a

    print("YES" if split_sort(s) == split_sort(t) else "NO") 

solve()