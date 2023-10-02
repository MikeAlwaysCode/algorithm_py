import sys
from collections import *

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
    n, q = mint()
    
    def getPrimes(n: int, res: Counter):
        d = 2
        while d * d <= n:
            if n % d == 0:
                while n % d == 0:
                    res[d] += 1
                    n //= d
            if n == 1:
                break
            d += 1
        if n > 1:
            res[n] += 1
        return res
            
    cnt = Counter()
    x = n
    getPrimes(x, cnt)
    
    x = n
    cc = cnt.copy()
    for _ in range(q):
        qry = ints()
        if qry[0] == 2:
            x = n
            cc = cnt.copy()
        else:
            x *= qry[1]
            getPrimes(qry[1], cc)
            p = 1
            for v in cc.values():
                p *= (v + 1)
            print("YES" if x % p == 0 else "NO")
    print()

for _ in range(int(input())):
    solve()