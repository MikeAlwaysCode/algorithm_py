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
    nums = [0] + ints() + [n + 1]
    
    # dp[i][j]: 到第i个元素可以操作j段的最小操作
    dp = [[n] * (n + 1) for _ in range(n + 2)]
    dp[0] = [0] * (n + 1)

    for i in range(1, n + 2):
        for j in range(i):
            if nums[j] < nums[i]:
                if j + 1 == i:  # 第i个元素无需操作
                    for k in range(n + 1):
                        dp[i][k] = min(dp[i][k], dp[j][k])
                else:   # 枚举k，把j至i之间的元素全部处理的操作
                    for k in range(n):
                        dp[i][k + 1] = min(dp[i][k + 1], dp[j][k] + i - j - 1)

        for j in range(1, n + 1):
            dp[i][j] = min(dp[i][j], dp[i][j - 1])

    print(*dp[n + 1][1:])

for _ in range(int(input())):
    solve()