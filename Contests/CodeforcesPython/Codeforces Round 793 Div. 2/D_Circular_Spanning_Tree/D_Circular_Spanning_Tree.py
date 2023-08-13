from collections import deque
import sys

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
    s = input()
    ans = []
    v = deque()
    i = 0
    while i < n:
        if s[i] == "0":
            j = i
            while j < n - 1 and s[j + 1] == "0":
                j += 1
            k = i
            while k != j:
                ans.append((k + 1, k + 2))
                k += 1
            if j < n - 1:
                ans.append((j + 1, j + 2))
                v.append(i + 1)
                i = j + 2
            elif not v:
                print("NO")
                return
            else:
                ans.append((j + 1, 1))
                v.append(i + 1)
                v.popleft()
                break
        else:
            v.append(i + 1)
            i += 1
    if len(v) & 1:
        print("NO")
    else:
        print("YES")
        for x, y in ans:
            print(x, y)
        v = list(v)
        for x in v[1:]:
            print(v[0], x)

for _ in range(int(input())):
    solve()