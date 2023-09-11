import sys

# from collections import *
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
    s = sum(nums)
    if s % n:
        print("No")
        return
    
    s //= n
    cnt = [0] * 31
    for x in nums:
        if x == s:
            continue
        else:
            d = abs(x - s)
            p = d & -d
            q = p + d
            
            if bin(q).count('1') != 1:
                print("No")
                return

            p = len(bin(p)) - 2
            q = len(bin(q)) - 2

            if x < s:
                cnt[p] -= 1
                cnt[q] += 1
            else:
                cnt[p] += 1
                cnt[q] -= 1
                
    print("No" if any(cnt) else "Yes")

for _ in range(int(input())):
    solve()