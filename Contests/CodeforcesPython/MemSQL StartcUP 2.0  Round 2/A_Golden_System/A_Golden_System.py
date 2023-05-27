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
    s1 = list(map(int, list(input())))
    s2 = list(map(int, list(input())))

    n = max(len(s1), len(s2))

    if n == 1:
        print(">" if s1[0] > s2[0] else "=" if s1[0] == s2[0] else "<")
        return

    if len(s1) < n: s1 = [0] * (n - len(s1)) + s1
    if len(s2) < n: s2 = [0] * (n - len(s2)) + s2

    for i in range(n - 2):
        mn = min(s1[i], s2[i])
        s1[i] -= mn
        s2[i] -= mn

        s1[i + 1] += s1[i]
        s1[i + 2] += s1[i]
        s2[i + 1] += s2[i]
        s2[i + 2] += s2[i]

        s1[i] = 0
        s2[i] = 0

    x, y = s1[-2] - s2[-2], s1[-1] - s2[-1]

    if x == 0:
        print(">" if y > 0 else "=" if y == 0 else "<")
    elif x * y > 0:
        print(">" if x > 0 else "<")
    else:
        l = 5 * x * x
        r = (- 2 * y - x) * (- 2 * y - x)
        if x < 0: l, r = r, l
        print(">" if l > r else "=" if l == r else "<")

# for _ in range(int(input())):
solve()