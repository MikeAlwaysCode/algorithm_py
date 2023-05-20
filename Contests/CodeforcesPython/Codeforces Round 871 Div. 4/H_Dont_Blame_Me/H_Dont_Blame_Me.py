import math
import sys
from bisect import *
from collections import *
from functools import *
from heapq import *
from itertools import *
from random import *
from string import *

# region fastio
input = lambda: sys.stdin.readline().rstrip()
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998244353
MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def solve() -> None:
    n, k = map(int, input().split())
    arr = ints()
    cnt = [0] * 64
    for a in arr:
        cnt[a] += 1

    for i in range(6):
        bit = 1 << i
        for j in range(64):
            if not j & bit:
                cnt[j] += cnt[j | bit]
    
    dp = [pow(2, cnt[i], MOD) for i in range(64)]

    for i in range(6):
        bit = 1 << i
        for j in range(64):
            if not j & bit:
                dp[j] -= dp[j | bit]
    
    ans = 0
    # for i in range(64):
    #     # if i.bit_count() == k:
    #     if bin(i)[2:].count("1") == k:
    #         ans += dp[i]
            
    for p in combinations(range(6), k):
        cur = 0
        for j in p:
            cur |= ( 1 << j )
        ans += dp[cur]
    
    if k == 6: ans -= 1
    
    print(ans % MOD)


for _ in range(int(input())):
    solve()

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
# from types import GeneratorType
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