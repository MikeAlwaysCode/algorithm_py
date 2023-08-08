import math
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

MOD = 998244353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def solve() -> None:
    n, m = mint()
    
    # 阶乘
    fact = [1] * (m + 1)
    for i in range(1, m + 1):
        fact[i] = fact[i-1] * i % MOD
    # 逆元
    inverse = [0] * (m + 1)
    inverse[m] = pow(fact[m], MOD - 2, MOD)
    for i in range(m, 0, -1):
        inverse[i-1] = inverse[i] * i % MOD
    # 组合数
    def comb(n: int, m: int, MOD = MOD) -> int:
        if m < 0 or m > n:
            return 0
        return fact[n] * inverse[m] % MOD * inverse[n-m] % MOD

    # 因为必须有一对相等，所以从m个数中取n - 1个数
    # 再除去最大的数，从n - 2个数中选择一个两边均有的数
    p = comb(m, n - 1) % MOD * (n - 2) % MOD

    # 452 ms
    # ans = p # 最大的数在位置1，除去相等的数，其余数在右边
    # for i in range(n - 3):
    #     # 枚举最大的数所处的位置
    #     p = p * (n - 3 - i) % MOD * pow(i + 1, MOD - 2, MOD) % MOD
    #     ans += p
    #     ans %= MOD

    # 61 ms
    # 从n - 3个数中，枚举每个数是否在最大的数左边
    ans = p * pow(2, n - 3, MOD) % MOD

    print(ans)

solve()