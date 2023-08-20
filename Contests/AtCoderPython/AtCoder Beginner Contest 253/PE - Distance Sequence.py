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
    if k == 0:
        print(pow(m, n, MOD))
        return

    '''
    # 100 ms
    dp = [1] * m
    for _ in range(n - 1):
        ndp = [0] * m
        for i in range(m - k):
            ndp[i + k] = (dp[i] + ndp[i + k - 1]) % MOD
        i, j = 0, m - 1
        while i <= j:
            ndp[i] = ndp[j] = (ndp[i] + ndp[j]) % MOD
            i += 1
            j -= 1
        dp = ndp
    print(sum(dp) % MOD)
    '''

    dp = list(range(m + 1))
    for _ in range(n - 1):
        ndp = [0] * (m + 1)
        for i in range(m):
            ndp[i + 1] = (ndp[i] + (dp[-1] - dp[min(i + k, m)] + dp[max(i - k + 1, 0)])) % MOD
        dp = ndp
    print(dp[-1])

solve()