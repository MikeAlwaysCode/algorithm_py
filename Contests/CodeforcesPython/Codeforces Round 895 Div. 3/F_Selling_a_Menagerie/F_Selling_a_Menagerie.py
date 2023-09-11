import math
import sys
from collections import *

# import itertools
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
    c = ints()
    deg = [0] * n

    for i in range(n):
        nums[i] -= 1
        deg[nums[i]] += 1

    ans = []
    q = deque(i for i in range(n) if deg[i] == 0)
    seen = [False] * n
    while q:
        x = q.popleft()
        ans.append(x + 1)
        seen[x] = True
        deg[nums[x]] -= 1
        if deg[nums[x]] == 0:
            q.append(nums[x])
    
    for i in range(n):
        if seen[i]: continue
        path = []
        mx = math.inf
        idx = 0
        while not seen[i]:
            path.append(i)
            seen[i] = True
            if c[i] < mx:
                mx = c[i]
                idx = len(path)
            i = nums[i]
        for x in path[idx:]:
            ans.append(x + 1)
        for x in path[:idx]:
            ans.append(x + 1)

    print(*ans)

for _ in range(int(input())):
    solve()