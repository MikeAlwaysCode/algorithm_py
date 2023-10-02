import math
import sys
# from functools import cache

# import itertools
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

fact = []
for i in range(3, 15):
    fact.append(math.factorial(i))

s = [0] * (1 << len(fact))
cnt = [0] * (1 << len(fact))
for mask in range(1, 1 << len(fact)):
    lb = mask & -mask
    cnt[mask] = cnt[mask - lb] + 1
    s[mask] = s[mask - lb] + fact[len(bin(lb)) - 3]
    '''
    for j in range(len(fact)):
        if (mask >> j) & 1:
            cnt[mask] += 1
            s[mask] += fact[j]
    '''

def solve() -> None:
    n = sint()

    def zz(x: int) -> int:
        return bin(x)[2:].count("1")
    
    ans = zz(n)
    
    for mask in range(1, 1 << len(fact)):
        if s[mask] > n: break
        ans = min(ans, cnt[mask] + zz(n - s[mask]))
    
    print(ans)

for _ in range(int(input())):
    solve()