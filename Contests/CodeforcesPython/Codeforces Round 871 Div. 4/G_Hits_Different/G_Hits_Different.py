import sys
from bisect import *
from collections import *
from functools import *
from heapq import *
from itertools import *
from math import *
from random import *
from string import *

# region fastio
input = lambda: sys.stdin.readline().rstrip()
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998244353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))


cnt = [0] * (3 * 10 ** 7)
def init():
    l = r = 0
    for i in range(1, 2024):
        nl = r + 1
        nr = r + i
        cnt[nl] = cnt[l] + nl * nl
        cnt[nr] = cnt[r] + nr * nr
        for j in range(nl + 1, nr):
            cnt[j] = j * j + cnt[j - i] + cnt[j - i + 1] - cnt[j - i * 2 + 2]
        l, r = nl, nr
    # print(row[:15])

def solve() -> None:
    n = int(input())
    print(cnt[n])

init()
for _ in range(int(input())):
    solve()

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