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
    n, q = mint()
    arr = ints()
    krr = ints()
    

    arr.sort()
    ans = [0] * q

    dp = [0] * (n + 1)
    dp[0] = arr[0]
    s = 0
    for i in range(1, n + 1):
        dp[i] = min(dp[i - 1] + 1, arr[i - 1] + 1)
        if i < n:
            dp[i] = min(dp[i], arr[i])
        s += arr[i - 1]

    ns = (n + 1) * n // 2
    mx_neg = ns + s - dp[-1] * n

    for i in range(q):
        k = krr[i]
        if k <= n:
            ans[i] = dp[k]
            continue
        
        k -= n
        if k & 1:
            res = min(dp[-2] + k + 1, arr[-1])
            ns = (k * 2 + n + 2) * (n - 1) // 2
            mx_neg2 = ns + s - res * n
            neg = (k + 1) // 2 - mx_neg2
        else:
            res = dp[-1] + k
            neg = k // 2 - mx_neg

        if neg > 0:
            res -= (neg + n - 1) // n

        ans[i] = res

    print(*ans)

# for _ in range(int(input())):
solve()