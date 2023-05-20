from contextlib import AsyncExitStack
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

def bit_count(x):
    x = (x & 0x55555555) + ((x >> 1) & 0x55555555)
    x = (x & 0x33333333) + ((x >> 2) & 0x33333333)
    x = (x & 0x0f0f0f0f) + ((x >> 4) & 0x0f0f0f0f)
    x = (x & 0x00ff00ff) + ((x >> 8) & 0x00ff00ff)
    x = (x & 0x0000ffff) + ((x >> 16) & 0x0000ffff)
    return x

def solve() -> None:
    n, m, k = mint()
    arr = ints()
    c = [[0] * n for _ in range(n)]
    for _ in range(k):
        x, y, z = mint()
        c[x - 1][y - 1] = z
    
    b = [1]
    for _ in range(n):
        b.append(2 * b[-1])
    
    dp = [[0] * n for _ in range(b[-1])]
    for mask in range(b[-1] - 1):
        for x in range(n):
            if not mask & b[x]: continue
            for y in range(n):
                if mask & b[y]: continue
                dp[mask|b[y]][y] = max(dp[mask|b[y]][y], dp[mask][x] + c[x][y])
    
    ans = 0
    for mask in range(b[-1]):
        # if mask.bit_count() != m: continue
        if bit_count(mask) ^ m: continue
        s1 = s2 = 0
        for i in range(n):
            s1 = max(s1, dp[mask][i])
            if mask & b[i]: s2 += arr[i]
        ans = max(ans, s1 + s2)
    print(ans)

# for _ in range(int(input())):
solve()