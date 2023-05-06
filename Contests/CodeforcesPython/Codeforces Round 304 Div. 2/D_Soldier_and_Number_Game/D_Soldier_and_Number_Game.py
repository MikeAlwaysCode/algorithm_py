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

mxn = 5 * 10 ** 6
factor = [0] * (mxn + 1)
# cnt = [1] * (mxn + 1)
# pres = [0] * (mxn + 1)
def init():
    for i in range(2, mxn + 1):
        # if factor[i] != 1:
        if factor[i] != 0:
            continue
        cnt = 1
        for j in range(i, mxn + 1, i):
            # factor[j] = i
            factor[j] = factor[cnt] + 1
            cnt += 1
            
    for i in range(2, mxn + 1):
        # if factor[i] != i:
        #     cnt[i] = cnt[i // factor[i]] + 1
        # pres[i] = pres[i - 1] + cnt[i]
        # pres[i] = pres[i - 1] + factor[i]
        factor[i] += factor[i - 1]

def solve() -> None:
    a, b = map(int, input().split())
    # print(pres[a] - pres[b])
    print(factor[a] - factor[b])

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