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
    n, k = mint()
    ans = 0
    '''
    # 状态不会到k，k - 1会直接转移到0
    dp = [[0] * k for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(n):
        cur = 0
        for j in range(k - 1, 0, -1):
            cur = (cur + dp[i][j]) % MOD
            # 前i个数构造大于等于j的子数组都能直接转移到i + 1的j
            dp[i + 1][j] = cur
        for j in range(k - 1, -1, -1):
            nxt = (j + 1) % k
            # 可以选择一个未出现的数(k - j)转移至j + 1
            dp[i + 1][nxt] = (dp[i + 1][nxt] + dp[i][j] * (k - j) % MOD) % MOD
        # 计算贡献
        ans = (ans + dp[i + 1][0] * pow(k, n - i - 1, MOD)) % MOD
    '''
    dp = [0] * k
    dp[0] = 1
    pk = pow(k, n - 1, MOD)
    inv = pow(k, MOD - 2, MOD)
    for i in range(n):
        tmp = dp[-1]
        for j in range(k - 2, -1, -1):
            dp[j], dp[j + 1] = (dp[j] + dp[j + 1]) % MOD, (dp[j + 1] + dp[j] * (k - j) % MOD) % MOD
        dp[0] = tmp
        ans = (ans + dp[0] * pk) % MOD
        pk = pk * inv % MOD
    
    print(ans)

solve()