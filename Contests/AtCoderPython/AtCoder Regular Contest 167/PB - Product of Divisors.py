import sys

# import math
# from bisect import *
# from collections import *
# from functools import *
# from heapq import *
# from itertools import *
# from random import *
# from string import *
# from types import GeneratorType

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

MOD = 998244353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))


def solve() -> None:
    a, b = mint()
    if b == 0:
        print(0)
        return
    primes = []
    d = 2
    while d * d <= a:
        if a % d == 0:
            primes.append(0)
            while a % d == 0:
                primes[-1] += 1
                a //= d
        if a == 1: break
        d += 1
    if a > 1:
        primes.append(1)
        
    k = primes[0] * b
    k = k * (k + 1) // 2
    ans, d = divmod(k, primes[0])
    for c in primes[1:]:
        ans = ans * (c * b + 1) % MOD
        d = d * (c * b + 1)
    ans = (ans + d // primes[0]) % MOD
    print(ans)

solve()