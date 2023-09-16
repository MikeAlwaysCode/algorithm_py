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
    n, k = mint()
    nums = ints()
    if k == 1:
        for i, x in enumerate(nums, 1):
            if i != x:
                print("NO")
                return
        print("YES")
        return

    # Timestamp 186 ms
    time = [0] * n
    clock = 1
    for x, t in enumerate(time):
        if t: continue
        start_time = clock
        while time[x] == 0:
            time[x] = clock
            clock += 1
            x = nums[x] - 1
        if time[x] >= start_time:
            if clock - time[x] != k:
                print("NO")
                return

    print("YES")
    
    '''
    # TopoSort 467 ms
    g = [[] for _ in range(n)]
    deg = [0] * n
    for i, x in enumerate(nums):
        g[i].append(x - 1)
        deg[x - 1] += 1
    seen = [False] * n
    q = deque(i for i in range(n) if deg[i] == 0)
    while q:
        u = q.popleft()
        seen[u] = True
        for v in g[u]:
            deg[v] -= 1
            if deg[v] == 0:
                q.append(v)
    
    for i in range(n):
        if seen[i]: continue
        cnt = 0
        while not seen[i]:
            cnt += 1
            seen[i] = True
            i = nums[i] - 1
        if cnt != k:
            print("NO")
            return

    print("YES")
    '''

for _ in range(int(input())):
    solve()