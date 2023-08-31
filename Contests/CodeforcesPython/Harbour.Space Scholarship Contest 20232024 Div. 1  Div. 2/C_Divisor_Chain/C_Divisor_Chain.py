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
    x = sint()
    ans = [x]
    
    def getPrimes(n: int) -> list[int]:
        primes = []
        d = 2
        while d * d <= n:
            if n % d == 0:
                while n % d == 0:
                    primes.append(d)
                    n //= d
            if n == 1:
                break
            d += 1
        if n > 1:
            primes.append(n)
        return primes
    primes = getPrimes(x)
    if primes[0] == x:
        x -= 1
        ans.append(x)
        primes = getPrimes(x)
    cnt2 = 0
    for p in primes:
        if p == 2:
            cnt2 += 1
            continue
        else:
            while p > 1:
                if p & 1:
                    x -= x // p
                    ans.append(x)
                    p -= 1
                else:
                    cnt2 += 1
                    p //= 2
    while cnt2 > 1:
        x //= 2
        cnt2 -= 1
        ans.append(x)
    
    if cnt2 == 1:
        ans.append(1)

    print(len(ans))
    print(*ans)

for _ in range(int(input())):
    solve()