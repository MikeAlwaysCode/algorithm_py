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
    arr = ints()
    # dp = defaultdict(int)
    dp = [[[Counter() for _ in range(2)] for _ in range(2)] for _ in range(30)]
    ans = 0
    for i, a in enumerate(arr):
        mx = 0
        hxor, xa, xi = (a ^ i) >> 1, a, i
        for bit in range(30):
            xora = xa & 1
            xori = xi & 1
            # mx = max(mx, dp[(bit, hxor, xora ^ 1, xori)])
            mx = max(mx, dp[bit][xora ^ 1][xori][hxor])
            hxor >>= 1
            xa >>= 1
            xi >>= 1
        mx += 1
        ans = max(ans, mx)
        hxor, xa, xi = (a ^ i) >> 1, a, i
        for bit in range(30):
            xora = xa & 1
            xori = xi & 1
            # dp[(bit, hxor, xori, xora)] = max(dp[(bit, hxor, xori, xora)], mx)
            dp[bit][xori][xora][hxor] = max(dp[bit][xori][xora][hxor], mx)
            hxor >>= 1
            xa >>= 1
            xi >>= 1

    print(ans)

for _ in range(int(input())):
    solve()