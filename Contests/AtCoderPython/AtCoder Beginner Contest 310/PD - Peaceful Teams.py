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
    n, t, m = mint()
    ban = [0] * n
    for _ in range(m):
        u, v = mint()
        u -= 1
        v -= 1
        ban[u] |= 1 << v
        ban[v] |= 1 << u

    possible = [False] * (1 << n)
    for mask in range(1 << n):
        m = 0
        for i in range(n):
            if (mask >> i) & 1: m |= ban[i]
        if not (mask & m): possible[mask] = True

    dp = [[0] * (1 << n) for _ in range(t + 1)]
    dp[0][0] = 1
    for mask in range(1 << n):
        new = nxt = mask | (mask + 1)
        while new < (1 << n):
            if possible[new ^ mask]:
                for i in range(t):
                    dp[i + 1][new] += dp[i][mask]
            new = (new + 1) | nxt
    print(dp[-1][-1])

solve()