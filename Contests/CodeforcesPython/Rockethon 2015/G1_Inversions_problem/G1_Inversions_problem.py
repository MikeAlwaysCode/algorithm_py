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
    n, k = mint()
    nums = ints()

    tot = n * (n + 1) // 2
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            dp[i][j] = int(nums[i] > nums[j])

    for _ in range(k):
        ndp = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                for l in range(n):
                    for r in range(l, n):
                        ni = l + r - i if l <= i <= r else i
                        nj = l + r - j if l <= j <= r else j
                        if ni < nj:
                            ndp[i][j] += dp[ni][nj] / tot
                        else:
                            ndp[i][j] += (1 - dp[nj][ni]) / tot
        dp = ndp
    
    ans = 0
    for i in range(n):
        for j in range(n):
            ans += dp[i][j]

    print(ans)

# for _ in range(int(input())):
solve()