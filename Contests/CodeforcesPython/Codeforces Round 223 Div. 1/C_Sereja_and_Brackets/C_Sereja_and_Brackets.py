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
    s = input()
    n = len(s)
    
    a = [0] * (n * 2)
    b = [0] * (n * 2)
    c = [0] * (n * 2)
    for i, ch in enumerate(s):
        if ch == "(":
            b[i + n] = 1
        else:
            c[i + n] = 1
    for i in range(n - 1, -1, -1):
        t = min(b[i << 1], c[i << 1 | 1])
        a[i] = a[i << 1] + a[i << 1 | 1] + t
        b[i] = b[i << 1] + b[i << 1 | 1] - t
        c[i] = c[i << 1] + c[i << 1 | 1] - t
    # print(a)
    # print(b)
    # print(c)
    q = sint()
    for _ in range(q):
        l, r = mint()
        l += n - 1
        r += n - 1
        la = lb = lc = ra = rb = rc = 0
        while l <= r:
            if l & 1:
                t = min(lb, c[l])
                la += a[l] + t
                lb += b[l] - t
                lc += c[l] - t
                l += 1
            if not r & 1:
                t = min(b[r], rc)
                ra += a[r] + t
                rb += b[r] - t
                rc += c[r] - t
                r -= 1
            l >>= 1
            r >>= 1
        t = min(lb, rc)
        print(2 * (la + ra + t))

# for _ in range(int(input())):
solve()