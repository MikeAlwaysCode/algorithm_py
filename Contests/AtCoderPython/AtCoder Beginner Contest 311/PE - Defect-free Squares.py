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
    h, w, n = mint()
    hole = set()
    for _ in range(n):
        x, y = mint()
        x -= 1
        y -= 1
        hole.add((x, y))
    ans = 0
    dp = [[1] * w for _ in range(h)]
    left = [[1] * w for _ in range(h)]
    up = [[1] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if (i, j) in hole:
                dp[i][j] = left[i][j] = up[i][j] = 0
                continue
            if j:
                left[i][j] += left[i][j - 1]
            if i:
                up[i][j] += up[i - 1][j]
            if i and j:
                dp[i][j] += min(left[i][j - 1], up[i - 1][j], dp[i - 1][j - 1])
            ans += dp[i][j]
    print(ans)

solve()