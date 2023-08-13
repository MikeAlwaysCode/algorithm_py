import sys
from collections import *

# import itertools
# import math
# import os
# from bisect import bisect, bisect_left
# from functools import reduce
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

    portal = []
    seg = []
    for _ in range(n):
        l, _, _, b = mint()
        seg.append((l, b))

    seg.sort(reverse = True)
    while seg:
        l, b = seg.pop()
        while seg and seg[-1][0] <= b:
            b = max(b, seg[-1][1])
            seg.pop()
        portal.append((l, b))
        
    q = sint()
    ans = [0] * q
    points = deque(sorted((x, i) for i, x in enumerate(ints())))

    for l, b in portal:
        while points and points[0][0] < b:
            x, i = points.popleft()
            if x < l:
                ans[i] = x
            else:   
                ans[i] = b
        
        if not points: break

    while points:
        x, i = points.popleft()
        ans[i] = x

    print(*ans)

for _ in range(int(input())):
    solve()