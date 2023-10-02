import math
import sys

# from bisect import *
# from collections import *
# from functools import *
# from heapq import *
# from itertools import *
# from random import *
# from string import *
# from types import GeneratorType

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
    n, k, p = mint()
    mx = (p + 1) ** k
    dp = [math.inf] * mx
    dp[0] = 0
    for _ in range(n):
        nums = ints()
        c = nums[0]
        op = nums[1:]
        for mask in range(mx - 1, -1, -1):
            nmask = 0
            x = mask
            pw = 1
            for i in range(k):
                nmask += max(0, (x % (p + 1)) - op[i]) * pw
                x //= (p + 1)
                pw *= (p + 1)
            dp[mask] = min(dp[mask], dp[nmask] + c)
    ans = math.inf
    for mask, v in enumerate(dp):
        if v == math.inf: continue
        check = True
        for i in range(k):
            if mask % (p + 1) < p:
                check = False
                break
            mask //= (p + 1)
        if check: ans = min(ans, v)
    print(-1 if ans == math.inf else ans)


solve()