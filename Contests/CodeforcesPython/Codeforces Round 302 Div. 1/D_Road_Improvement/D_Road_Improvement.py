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
MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def solve() -> None:
    n = sint()
    parent = [-1] + ints()

    tree = [[] for _ in range(n)]
    for i in range(1, n):
        tree[parent[i] - 1].append(i)
    
    dp = [1] * n
    for i in range(n-1, 0, -1):
        dp[parent[i] - 1] *= dp[i] + 1
        dp[parent[i] - 1] %= MOD
    
    dp_from_up = [1] * n
    for i in range(n):
        
        pref_mul = [1]
        for j in tree[i]:
            pref_mul.append(pref_mul[-1] * (dp[j] + 1) % MOD)
        
        suff_mul = [1]
        for j in reversed(tree[i]):
            suff_mul.append(suff_mul[-1] * (dp[j] + 1) % MOD)
    
        suff_mul.reverse()
        for j in range(len(tree[i])):
            dp_from_up[tree[i][j]] = (dp_from_up[i] * pref_mul[j] * suff_mul[j+1] + 1) % MOD
    
    print(*(x * y % MOD for x, y in zip(dp, dp_from_up)))

solve()
