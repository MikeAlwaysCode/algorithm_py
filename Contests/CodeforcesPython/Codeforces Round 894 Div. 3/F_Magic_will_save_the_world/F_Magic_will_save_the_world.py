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
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def solve() -> None:
    w, f = mint()
    n = sint()
    nums = ints()
    s = sum(nums)

    def cal(x: int) -> int:
        return min(max((x + w - 1) // w, (s - x + f - 1) // f), max((x + f - 1) // f, (s - x + w - 1) // w))
    
    ans = min((s + w - 1) // w, (s + f - 1) // f)
    dp = [False] * (s + 1)
    dp[0] = True
    for x in nums:
        for j in range(s, x - 1, -1):
            if dp[j - x]:
                dp[j] = True
                ans = min(ans, cal(j))
    print(ans)

    '''
    mx = max(nums)
    l = 1
    r = min((s + w - 1) // w, (s + f - 1) // f)
    def check(x: int) -> bool:
        vw, vf = w * x, f * x
        if mx > vw and mx > vf: return False
        if vw >= s or vf >= s: return True
        dp = [False] * (vw + 1)
        dp[0] = True
        for x in nums:
            for j in range(vw, x - 1, -1):
                if dp[j - x]:
                    dp[j] = True
                    if vf >= s - j: return True
        return False

    while l < r:
        mid = (l + r) >> 1
        if check(mid):
            r = mid
        else:
            l = mid + 1
    print(r)
    '''

for _ in range(int(input())):
    solve()