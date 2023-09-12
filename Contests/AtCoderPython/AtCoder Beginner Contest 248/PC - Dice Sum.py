import sys

# import math
# from bisect import *
# from collections import *
# from functools import *
# from heapq import *
# from itertools import *
# from random import *
# from string import *
# from types import GeneratorType

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
    # dp[i]: 和是i的方案数
    dp = [0] * (k + 1)
    dp[0] = 1
    for i in range(n):
        # 和最大是k和(i + 1)个m的较小值
        up = min(k, m * (i + 1))
        # 最后m个数的方案和
        s = sum(dp[up - m + 1:up + 1]) % MOD
        for j in range(up, -1, -1):
            # 滑窗处理
            if j - m >= 0:
                s += dp[j - m]
            s -= dp[j]
            dp[j] = s
    print(sum(dp) % MOD)
    '''
    # 后缀和优化
    suff = [0] * (k + 2)
    suff[0] = 1
    for i in range(n):
        for j in range(min(k, m * (i + 1)), -1, -1):
            s = suff[max(j - m, 0)] - suff[j]
            suff[j] = (suff[j + 1] + s) % MOD
    print(suff[0]) 

solve()