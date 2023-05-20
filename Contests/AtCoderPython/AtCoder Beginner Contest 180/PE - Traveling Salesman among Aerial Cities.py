from cmath import inf
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
    p = []
    for _ in range(n):
        x, y, z = mint()
        p.append((x, y, z))
    
    cost = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j: continue
            cost[i][j] = abs(p[i][0] - p[j][0]) + abs(p[i][1] - p[j][1]) + max(0, p[j][2] - p[i][2])
    
    dp = [[math.inf] * n for _ in range(1 << n)]
    dp[1][0] = 0
    for s in range(1, 1 << n, 2):
        for i in range(n):
            if dp[s][i] == math.inf: continue
            for j in range(n):
                if (s >> j) & 1: continue
                dp[s | (1 << j)][j] = min(dp[s | (1 << j)][j], dp[s][i] + cost[i][j])

    ans = math.inf
    for i in range(n):
        if dp[(1 << n) - 1][i] == math.inf: continue
        ans = min(ans, dp[(1 << n) - 1][i] + cost[i][0])
    
    print(ans)

solve()