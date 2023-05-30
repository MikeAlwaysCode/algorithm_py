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
    n, m = mint()
    nums = [0] * (1 << n) + ints()

    op = [n & 1, n & 1 ^ 1] # n - 1: True -> or, n - 2: Fals -> xor
    for i in range(n - 1, -1, -1):
        for j in range(1 << i, 1 << (i + 1)):
            nums[j] = nums[j << 1] | nums[j << 1 | 1] if op[i & 1] else nums[j << 1] ^ nums[j << 1 | 1]
    
    for _ in range(m):
        p, b = mint()
        p += (1 << n) - 1
        nums[p] = b
        for i in range(n - 1, -1, -1):
            p >>= 1
            nums[p] = nums[p << 1] | nums[p << 1 | 1] if op[i & 1] else nums[p << 1] ^ nums[p << 1 | 1]
        print(nums[1])


# for _ in range(int(input())):
solve()