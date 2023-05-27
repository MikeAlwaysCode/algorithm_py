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
    n, mod = mint()
    nums = ints()

    # meet-in-the-middle
    m = (n + 1) >> 1
    # 单独选前m个数的值
    bit = {1 << i:nums[i] % mod for i in range(m)}
    dp = [0] * (1 << m)
    for mask in range(1, 1 << m):
        # 从不包含lb元素的子集 + lb元素转移
        dp[mask] = (dp[mask ^ mask & -mask] + bit[mask & -mask]) % mod
    
    res1 = sorted(list(set(dp)))

    k = n - m
    bit = {1 << i:nums[i + m] % mod for i in range(k)}
    dp = [0] * (1 << k)

    # 双指针 265 ms
    for mask in range(1, 1 << k):
        dp[mask] = (dp[mask ^ mask & -mask] + bit[mask & -mask]) % mod
    res2 = sorted(list(set(dp)))
    
    ans = (res1[-1] + res2[-1]) % mod
    i, j = 0, len(res2) - 1
    while i < len(res1) and j >= 0:
        while res1[i] + res2[j] >= mod:
            j -= 1
        ans = max(ans, res1[i] + res2[j] % mod)
        i += 1

    '''
    # 二分 233 ms
    ans = res1[-1]
    for mask in range(1, 1 << k):
        dp[mask] = (dp[mask ^ mask & -mask] + bit[mask & -mask]) % mod
        # 两个小于mod的最大数相加<2mod 可能是答案
        ans = max(ans, (res1[-1] + dp[mask]) % mod)
        # 查找小于且最接近mod - s的数
        j = bisect(res1, mod - dp[mask] - 1)
        if j: ans = max(ans, (res1[j - 1] + dp[mask]) % mod)
    '''

    print(ans)

# for _ in range(int(input())):
solve()