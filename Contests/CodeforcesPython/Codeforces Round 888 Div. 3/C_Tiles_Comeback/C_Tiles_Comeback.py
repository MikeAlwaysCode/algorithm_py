import sys

# import itertools
# import math
# import os
# import random
# from bisect import bisect, bisect_left
# from collections import *
# from functools import reduce
# from heapq import heapify, heappop, heappush
# from io import bytesio, iobase
# from string import *

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# print = lambda d: sys.stdout.write(str(d) + "\n")
# endregion fastio

# # region interactive
# def printqry(a, b) -> none:
#     sa = str(a)
#     sb = str(b)
#     print(f"? {sa} {sb}", flush = true)

# def printans(ans) -> none:
#     s = str(ans)
#     print(f"! {s}", flush = true)
# # endregion interactive

# # region dfsconvert
# from types import generatortype
# def bootstrap(f, stack=[]):
#     def wrappedfunc(*args, **kwargs):
#         if stack:
#             return f(*args, **kwargs)
#         else:
#             to = f(*args, **kwargs)
#             while true:
#                 if type(to) is generatortype:
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

# mod = 998244353
# mod = 10 ** 9 + 7
# dir = ((-1, 0), (0, 1), (1, 0), (0, -1))

def solve() -> None:
    n, k = mint()
    nums = ints()
    s, t = nums[0], nums[-1]
    fr, to = n, -1
    scnt = tcnt = 0
    for i in range(n):
        if nums[i] == s:
            scnt += 1
            if scnt == k:
                fr = i
                break
    if s == t and fr < n:
        print("YES")
        return

    for i in range(n - 1, -1, -1):
        if nums[i] == t:
            tcnt += 1
            if tcnt == k:
                to = i
                break
    
    print("YES" if fr < to else "NO")

for _ in range(int(input())):
    solve()