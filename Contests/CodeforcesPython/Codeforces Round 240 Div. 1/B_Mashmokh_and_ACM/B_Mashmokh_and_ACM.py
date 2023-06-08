import math
import sys
from bisect import *
from collections import *
from functools import *
from heapq import *
from itertools import *
from random import *
from string import *
from types import GeneratorType

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

# MOD = 998244353
MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def solve() -> None:
    k, n = mint()
    ks = [[] for _ in range(k + 1)]  # ks[x] 为 x 分解质因数后，每个质因数的个数列表
    for i in range(2, k + 1):
        p, x = 2, i
        while p * p <= x:
            if x % p == 0:
                c = 1
                x //= p
                while x % p == 0:
                    c += 1
                    x //= p
                ks[i].append(c)
            p += 1
        if x > 1: ks[i].append(1)
    
    ans = 0
    for x in range(1, k + 1):
        mul = 1
        for c in ks[x]:
            mul = mul * math.comb(n + c - 1, c) % MOD
        ans = (ans + mul) % MOD
    print(ans)

    '''
    dp = [1] * (k + 1)
    dp[0] = 0
    for _ in range(n - 1):
        for i in range(k, 0, -1):
            for j in range(i * 2, k + 1, i):
                dp[j] = (dp[j] + dp[i]) % MOD
    
    print(sum(dp) % MOD)
    '''

# for _ in range(int(input())):
solve()