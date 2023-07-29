import sys
from bisect import bisect

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
    n, m = mint()
    s = input()
    ans = set()
    left, right = [-1] * n, [n] * n
    last = -1
    for i in range(n):
        if s[i] == "0":
            last = i
        left[i] = last
    last = n
    for i in range(n - 1, -1, -1):
        if s[i] == "1":
            last = i
        right[i] = last
    for _ in range(m):
        l, r = mint()
        l = right[l - 1]
        r = left[r - 1]
        if r < l: ans.add((n, n))
        else: ans.add((l, r))

    '''
    one = [n] * n
    zero = []
    last = n
    for i in range(n - 1, -1, -1):
        if s[i] == "1":
            last = i
        else:
            zero.append(i)
        one[i] = last
    zero.reverse()
    for _ in range(m):
        l, r = mint()
        l -= 1
        r -= 1
        if not zero or len(zero) == n:
            ans.add((n, n))
            continue
        l = one[l]
        if r <= l:
            ans.add((n, n))
            continue
        i = bisect(zero, l)
        j = bisect(zero, r)
        if i == j: ans.add((n, n))
        else: ans.add((l, j))
    '''
    print(len(ans))

for _ in range(int(input())):
    solve()