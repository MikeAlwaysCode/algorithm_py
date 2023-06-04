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
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def solve() -> None:
    n = sint()
    nums = ints()

    # 1. 计算后缀最小和及下标k
    suff = [(0, n)] * (n + 1)
    s = 0
    for i in range(n - 1, -1, -1):
        s += nums[i]
        suff[i] = suff[i + 1]
        if s < suff[i][0]:
            suff[i] = (s, i)
    
    # 2. 计算最小子数组和及下标i, j
    ans, ai, aj, ak = 0, 0, 0, suff[0][1]
    mn = pre = i = j = mi = mj = 0
    
    for j in range(n):
        # 当前最小的s[i:j]
        pre += nums[j]
        if nums[j] < pre:
            pre, i = nums[j], j
        # 前缀最小的s[i:j]
        if pre < mn:
            mn, mi, mj = pre, i, j + 1
        # 最小的s[i:j] + s[k:n]
        if mn + suff[j + 1][0] < ans:
            ans = mn + suff[j + 1][0]
            ai, aj, ak = mi, mj, suff[j + 1][1]
    print(ai, aj, ak)

# for _ in range(int(input())):
solve()