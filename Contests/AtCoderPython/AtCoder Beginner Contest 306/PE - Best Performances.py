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
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def solve() -> None:
    n, k, q = mint()
    large, small = [], []
    nums = [0] * n
    ink = [False] * n
    s = cnt = 0
    for _ in range(q):
        x, y = mint()
        x -= 1
        if ink[x]:
            cnt -= 1
            s -= nums[x]
            ink[x] = False
        nums[x] = y
        heappush(small, (- y, x))
        while large and not ink[large[0][1]]:
            heappop(large)
        while small and (ink[small[0][1]] or small[0][0] != -nums[small[0][1]]):
            heappop(small)
        while small and (cnt < k or -small[0][0] > large[0][0]):
            if cnt == k:
                y, x = heappop(large)
                if not ink[x] or y != nums[x]: continue
                cnt -= 1
                s -= y
                ink[x] = False
                heappush(small, (- nums[x], x))
            y, x = heappop(small)
            y = - y
            if ink[x] or y != nums[x]: continue
            s += y
            heappush(large, (y, x))
            ink[x] = True
            cnt += 1
        print(s)

solve()