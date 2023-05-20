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
    s = input()
    n = sint()
    m = len(s)
    
    dp = [[0] * 2 for _ in range(62)]
    for bit in range(1, 62):
        if m - bit >= 0:
            c = s[m - bit]
        else:
            c = "0"
        
        d = n >> (bit - 1) & 1
        if c == "?":
            dp[bit][1] = dp[bit - 1][1] + (1 << (bit - 1))
            if d == 0:
                dp[bit][0] = dp[bit - 1][0]
            else:
                if dp[bit - 1][0] != -1:
                    dp[bit][0] = dp[bit - 1][0] + (1 << (bit - 1))
                else:
                    dp[bit][0] = dp[bit - 1][1]
        elif c == "1":
            dp[bit][1] = dp[bit - 1][1] + (1 << (bit - 1))
            if d == 0:
                dp[bit][0] = -1
            else:
                if dp[bit - 1][0] != -1:
                    dp[bit][0] = dp[bit - 1][0] + (1 << (bit - 1))
                else:
                    dp[bit][0] = dp[bit - 1][0]
        else: # c == "0"
            dp[bit][1] = dp[bit - 1][1]
            if d == 0:
                dp[bit][0] = dp[bit - 1][0]
            else:
                dp[bit][0] = max(dp[bit - 1][0], dp[bit - 1][1])
            
    print(dp[-1][0])

solve()