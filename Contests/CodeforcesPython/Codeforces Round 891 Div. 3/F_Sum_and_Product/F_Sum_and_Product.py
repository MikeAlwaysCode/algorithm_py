import math
import sys
from collections import *
from random import randint

# import itertools
# import math
# import os
# import random
# from bisect import bisect, bisect_left
# from functools import reduce
# from heapq import heapify, heappop, heappush
# from io import BytesIO, IOBase
# from string import *

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

# MOD = 998244353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def solve() -> None:
    n = sint()
    nums = ints()
    # nums.sort()
    # cnt = Counter(nums)
    h = randint(1, 1 << 30)
    cnt = Counter(x ^ h for x in nums)
    
    q = sint()
    ans = [0] * q
    for i in range(q):
        x, y = mint()
        # x = x1 + x2 = - b/a, y = x1 * x2 = c/a
        # t = x * x - 4 * y = (b^2 - 4ac) / a^2
        # 1. t == 0: x1 = x2 = -b/2a = x/2
        # 2. t > 0: x1 = x/2 + sqrt(t) / 2, x2 = x/2 - sqrt(t)
        t = x * x - 4 * y
        
        if t == 0:
            if x & 1: continue
            # ans[i] = cnt[x // 2] * (cnt[x // 2] - 1) // 2
            ans[i] = cnt[(x // 2) ^ h] * (cnt[(x // 2) ^ h] - 1) // 2
        elif t > 0:
            m = math.isqrt(t)
            if m * m != t: continue
            # ans[i] = cnt[(x - m) // 2] * cnt[(x + m) // 2]
            ans[i] = cnt[((x - m) // 2) ^ h] * cnt[((x + m) // 2) ^ h]
        
    print(*ans)

for _ in range(int(input())):
    solve()