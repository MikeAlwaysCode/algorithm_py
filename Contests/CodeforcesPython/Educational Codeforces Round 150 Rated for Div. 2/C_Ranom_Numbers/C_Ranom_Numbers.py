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

v = list(pow(10, i) for i in range(5))

def solve() -> None:
    s = list(ord(c) - 65 for c in input())
    s.reverse()
    n = len(s)
    first = [-1] * 5
    last = [-1] * 5
    for i, x in enumerate(s):
        if first[x] == -1: first[x] = i
        last[x] = i

    def f(nums: list) -> int:
        res = mx = 0
        for x in nums:
            if mx > x:
                res = res - v[x]
            else:
                res = res + v[x]
            mx = max(mx, x)
        return res
    ans = - math.inf

    for x in range(5):
        if first[x] == -1: continue
        for k in range(5):
            s[first[x]] = k
            ans = max(ans, f(s))
            s[first[x]] = x
            s[last[x]] = k
            ans = max(ans, f(s))
            s[last[x]] = x

    print(ans)

for _ in range(int(input())):
    solve()