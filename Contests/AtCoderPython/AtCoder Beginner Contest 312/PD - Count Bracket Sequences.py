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

MOD = 998244353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def solve() -> None:
    s = input()
    n = len(s)

    if n & 1:
        print(0)
        return

    dp = [0] * n
    dp[0] = 1
    for c in s:
        tmp = [0] * n
        for i in range(n // 2 + 1):
            if c == "(":
                if (i + 1) * 2 <= n: tmp[i + 1] = (tmp[i + 1] + dp[i]) % MOD
            elif c == ")":
                if i: tmp[i - 1] = (tmp[i - 1] + dp[i]) % MOD
            else:
                if (i + 1) * 2 <= n: tmp[i + 1] = (tmp[i + 1] + dp[i]) % MOD
                if i: tmp[i - 1] = (tmp[i - 1] + dp[i]) % MOD
        dp = tmp
    print(dp[0])

solve()