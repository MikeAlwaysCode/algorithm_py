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

def bit_count(x):
    # x = (x & 0x55555555) + ((x >> 1) & 0x55555555)
    # x = (x & 0x33333333) + ((x >> 2) & 0x33333333)
    # x = (x & 0x0f0f0f0f) + ((x >> 4) & 0x0f0f0f0f)
    # x = (x & 0x00ff00ff) + ((x >> 8) & 0x00ff00ff)
    # x = (x & 0x0000ffff) + ((x >> 16) & 0x0000ffff)
    # return x
    res = 0
    while x:
        if x & 1: res += 1
        x >>= 1
    return res

def solve() -> None:
    n = sint()
    bits = bit_count(n)
    if bits == 3:
        print(n)
    elif bits > 3:
        for i in range(61):
            if n & (1 << i):
                n ^= 1 << i
                bits -= 1
                if bits == 3: break
        print(n)
    elif n < 7:
        print(-1)
    else:
        for i in range(2):
            if n & (1 << i):
                n ^= 1 << i
                bits -= 1
        for i in range(2, 61):
            if n & (1 << i):
                n ^= 1 << i
                for j in range(i - 1, i + bits - 5, -1):
                    n |= 1 << j
                break
        print(n)

for _ in range(sint()):
    solve()