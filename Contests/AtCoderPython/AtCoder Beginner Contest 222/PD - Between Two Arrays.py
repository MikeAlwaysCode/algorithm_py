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
    n = sint()
    A = ints()
    B = ints()
    # dp[i]：当前填小于等于i的方案数
    dp = [0] * 3001
    dp[A[0]] = 1
    for i in range(A[0] + 1, 3001):
        dp[i] = dp[i - 1]
        if i <= B[0]:
            dp[i] += 1
    for a, b in zip(A[1:], B[1:]):
        tmp = [0] * 3001
        tmp[a] = dp[a]
        for i in range(a + 1, 3001):
            tmp[i] = tmp[i - 1]
            if i <= b:
                # 当前可以填i，加上前一位dp[i]方案数
                tmp[i] = (tmp[i] + dp[i]) % MOD
        dp = tmp
    print(dp[-1])

solve()