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

def read_int():
    res = b''
 
    while True:
        d = sys.stdin.buffer.read(1)
        if d == b'-' or d.isdigit():
            res += d
        elif res:
            break
 
    return int(res)

def solve() -> None:
    # n, q = mint()
    # nums = ints()
    # qry = ints()
    n, q = read_int(), read_int()
    nums = [read_int() for _ in range(n)]
    qry = [read_int() for _ in range(q)]

    def count_le(x: int) -> int:
        cnt = 0
        for y in nums:
            if y <= x:
                cnt += 1
        for y in qry:
            if y > 0 and y <= x:
                cnt += 1
            if y < 0 and -y <= cnt:
                cnt -= 1
        return cnt

    if count_le(n) == 0:
        print(0)
        return
    
    l, r = 0, n
    while l < r:
        mid = (l + r) >> 1
        if count_le(mid):
            r = mid
        else:
            l = mid + 1
    print(r)

solve()