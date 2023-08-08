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

# region interactive
def printQry(a, b) -> None:
    sa = str(a)
    sb = str(b)
    print(f"? {sa} {sb}", flush = True)

def printAns(ans) -> None:
    s = str(ans)
    print(f"! {s}", flush = True)
# endregion interactive

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
    n, k = mint()
    nums = [0] * n
    xor = 0
    for i in range(k + 1):
        qry = []
        for j in range(k + 1):
            if j == i: continue
            qry.append(j + 1)
        print("?", *qry, flush = True)
        nums[i] = sint()
        xor ^= nums[i]
    for i in range(k + 1):
        nums[i] ^= xor
    xor ^= nums[k] ^ nums[k - 1]
    qry = list(range(1, k + 1))
    for i in range(k + 1, n):
        qry[-1] = i + 1
        print("?", *qry, flush = True)
        nums[i] = sint()
        nums[i] ^= xor
    
    print("!", *nums, flush = True)

solve()