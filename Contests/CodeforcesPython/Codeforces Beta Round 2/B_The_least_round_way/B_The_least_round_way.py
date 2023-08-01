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

# MOD = 998244353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def solve() -> None:
    n = sint()
    cnt2 = [[0] * n for _ in range(n)]
    cnt5 = [[0] * n for _ in range(n)]
    zi = zj = -1
    for i in range(n):
        nums = ints()
        for j, x in enumerate(nums):
            while x and x % 2 == 0:
                cnt2[i][j] += 1
                x //= 2
            while x and x % 5 == 0:
                cnt5[i][j] += 1
                x //= 5
            if i and j:
                cnt2[i][j] += min(cnt2[i - 1][j], cnt2[i][j - 1])
                cnt5[i][j] += min(cnt5[i - 1][j], cnt5[i][j - 1])
            elif i:
                cnt2[i][j] += cnt2[i - 1][j]
                cnt5[i][j] += cnt5[i - 1][j]
            elif j:
                cnt2[i][j] += cnt2[i][j - 1]
                cnt5[i][j] += cnt5[i][j - 1]
            
            if x == 0: zi, zj = i, j

    if cnt2[-1][-1] <= cnt5[-1][-1]:
        dp = cnt2
    else:
        dp = cnt5

    if dp[-1][-1] and zi != -1:
        ans = "D" * zi + "R" * zj + "D" * (n - 1 - zi) + "R" * (n - 1 - zj)
        print(1)
        print(ans)
        return
        
    ans = []
    x = y = n - 1
    while x != 0 or y != 0:
        if y == 0:
            x -= 1
            ans.append("D")
        elif x == 0:
            y -= 1
            ans.append("R")
        elif dp[x - 1][y] < dp[x][y - 1]:
            x -= 1
            ans.append("D")
        else:
            y -= 1
            ans.append("R")
        
    ans.reverse()
    print(dp[-1][-1])
    print("".join(ans))

solve()
