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
    a, b, n = mint()

    # 阶乘
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i-1] * i % MOD
    # 逆元
    inverse = [0] * (n + 1)
    inverse[n] = pow(fact[n], MOD - 2, MOD)
    for i in range(n, 0, -1):
        inverse[i-1] = inverse[i] * i % MOD
    # 组合数
    def comb(n: int, m: int, MOD = MOD) -> int:
        if m < 0 or m > n:
            return 0
        return fact[n] * inverse[m] % MOD * inverse[n-m] % MOD

    def isGood(x: int) -> bool:
        while x:
            if x % 10 != a and x % 10 != b:
                return False
            x //= 10
        return True

    ans = 0
    for i in range(n + 1):
        s = a * i + b * (n - i)
        if isGood(s):
            ans = (ans + comb(n, i)) % MOD
    print(ans)
    
solve()