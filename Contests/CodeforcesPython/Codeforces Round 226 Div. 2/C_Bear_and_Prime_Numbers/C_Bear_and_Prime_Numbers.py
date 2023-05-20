import math
import sys
from bisect import *
from collections import *
from functools import *
from heapq import *
from itertools import *
from random import *
from string import *

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# print = lambda d: sys.stdout.write(str(d) + " ")
# endregion fastio

# MOD = 998244353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def solve() -> None:
    n = sint()
    arr = ints()

    mxn = max(arr)

    # arr.sort()
    # cnt = Counter(arr)

    cnt = [0] * (mxn + 1)
    for a in arr:
        cnt[a] += 1

    factor = [1] * (mxn + 1)
    # primes = list()
    pres = [0] * (mxn + 1)
    
    for i in range(2, mxn + 1):
        pres[i] = pres[i - 1]
        if factor[i] != 1:
            continue
        # primes.append(i)
        pres[i] += cnt[i]
        for j in range(i + i, mxn + 1, i):
            factor[j] = i
            pres[i] += cnt[j]
    
    # print(primes)
    # print(pres)
    m = sint()
    for _ in range(m):
        l, r = mint()
        # r = bisect(primes, r)
        # l = bisect_left(primes, l)
        if l > mxn:
            print(0)
        else:
            print(pres[min(mxn, r)] - pres[l - 1])

# for _ in range(int(input())):
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