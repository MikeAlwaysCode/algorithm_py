import sys
import itertools

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

def check(x: int) -> bool:
    for i in itertools.count(2):
        if i * i > x: return True
        if x % i == 0: return False

def split(n: int) -> list:
    if check(n):
        return [n]
    
    x = 2
    while True:
        if check(n - x):
            break
        x += 1

    if check(x):
        return [x, n - x]
    
    isprime = [True] * (x + 1)
    primes = set()
    for i in range(2, x + 1):
        if isprime[i]:
            primes.add(i)
        for p in primes:
            if i * p > x:
                break
            isprime[i * p] = False
            if i % p == 0:
                break
    for p in primes:
        if x - p in primes:
            return [n - x, p, x - p]
        
def solve() -> None:
    n = sint()
    ans = split(n)
    print(len(ans))
    print(*ans)

solve()
