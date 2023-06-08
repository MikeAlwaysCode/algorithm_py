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
MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def solve() -> None:
    n, m, k = mint()
    nums = ints()
    ans = pow(k, m, MOD)

    # 逆元
    inverse = [0] * (n + 1)
    # inverse[n] = pow(n, MOD - 2, MOD)
    # for i in range(n, 0, -1):
    #     inverse[i-1] = inverse[i] * i % MOD
    inverse[0] = inverse[1] = 1
    # for i in range(2, n + 1):
    #     inverse[i] = (MOD - MOD // i) * inverse[MOD % i] % MOD

    # k^m - sum(C(m, i) * (k - 1) ^ (m - i))

    # 265 ms
    c = 1
    p = pow(k - 1, m, MOD)
    p_inv = pow(k - 1, MOD - 2, MOD)
    for i in range(n):
        ans = (ans - c * p % MOD) % MOD
        if i >= 1:  # 249 ms
            inverse[i + 1] = (MOD - MOD // (i + 1)) * inverse[MOD % (i + 1)] % MOD
        c = c * (m - i) * inverse[i + 1] % MOD
        p = p * p_inv % MOD

    # 248 ms
    # nums[0] = 1
    # # ans = (ans - pow(k - 1, m, MOD)) % MOD
    # for i in range(1, n):
    #     nums[i] = nums[i - 1] * (m - i + 1) * inverse[i] % MOD
    #     # ans = (ans - nums[i] * pow(k - 1, m - i, MOD) % MOD) % MOD
    # 
    # p = pow(k - 1, m - n, MOD)
    # for i in range(n - 1, -1, -1):
    #     p = p * (k - 1) % MOD
    #     ans = (ans - nums[i] * p % MOD) % MOD

    # # 1029 ms
    # c = 1
    # for i in range(n):
    #     ans = (ans - c * pow(k - 1, m - i, MOD) % MOD) % MOD
    #     c = c * (m - i) * pow(i + 1, MOD - 2, MOD) % MOD

    print(ans)

for _ in range(int(input())):
    solve()