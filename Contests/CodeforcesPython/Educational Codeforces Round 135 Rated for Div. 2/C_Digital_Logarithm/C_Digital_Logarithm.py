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
    A = ints()
    B = ints()

    ans = 0

    def check(x: int):
        nonlocal ans
        A.sort()
        B.sort()
        i = j = 0
        while i < n and j < n:
            if A[i] == B[j]:
                i += 1
                j += 1
            elif A[i] < B[j]:
                if A[i] > x:
                    A[i] = len(str(A[i]))
                    ans += 1
                i += 1
            else:
                if B[j] > x:
                    B[j] = len(str(B[j]))
                    ans += 1
                j += 1
        while i < n or j < n:
            if i < n:
                if A[i] > x:
                    A[i] = len(str(A[i]))
                    ans += 1
                i += 1
            if j < n:
                if B[j] > x:
                    B[j] = len(str(B[j]))
                    ans += 1
                j += 1

    check(9)
    check(1)

    print(ans)

for _ in range(int(input())):
    solve()