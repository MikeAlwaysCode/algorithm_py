import sys
from typing import Counter

# import itertools
# import math
# import os
# import random
# from bisect import bisect, bisect_left
# from collections import *
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
    nums = [0] + ints()

    s = (n + 1) * n // 2
    if nums[-1] != s:
        nums.append(s)

        for i in range(n, 0, -1):
            nums[i] -= nums[i - 1]
            if nums[i] <= 0 or nums[i] > n:
                print("NO")
                return
        
        print("YES" if len(set(nums)) == n + 1 else "NO")
        return
    
    x = []
    cnt = Counter()
    for i in range(n - 1, 0, -1):
        nums[i] -= nums[i - 1]
        if nums[i] <= 0:
            print("NO")
            return
        if nums[i] > n:
            x.append(nums[i])
        else:
            cnt[nums[i]] += 1
            if cnt[nums[i]] > 2:
                print("NO")
                return
            if cnt[nums[i]] > 1:
                x.append(nums[i])
        if len(x) > 1:
            print("NO")
            return

    if len(x) != 1:
        print("NO")
        return
    
    missing = []
    for i in range(1, n + 1):
        if cnt[i] == 0: missing.append(i)
    
    if len(missing) != 2 or x[0] != sum(missing):
        print("NO")
    else:
        print("YES")

for _ in range(int(input())):
    solve()