# import math
import sys

# import itertools
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

MOD = 998244353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def solve() -> None:
    n, m, k = mint()
    '''
    # 77 ms
    dp = [0] * (k + 1)
    dp[0] = m
    for _ in range(1, n):
        for i in range(k, 0, -1):
            dp[i] = (dp[i] + dp[i - 1] * (m - 1)) % MOD
    print(dp[-1])
    '''
    '''
    # 62 ms
    ans = math.comb(n - 1, k) % MOD
    ans = ans * m * pow(m - 1, k, MOD) % MOD
    print(ans)
    '''
    # 62 ms
    # 阶乘
    fact = 1
    for i in range(2, n):
        fact = fact * i % MOD
    ans = m * fact % MOD

    # 逆元
    inverse = pow(fact, MOD - 2, MOD)
    if k == n - 1 or k == 0: ans = ans * inverse % MOD
    for i in range(n - 1, 0, -1):
        inverse = inverse * i % MOD
        if i - 1 == k or i - 1 == n - 1 - k: ans = ans * inverse % MOD
    
    ans = ans * pow(m - 1, k, MOD) % MOD
    print(ans)

solve()