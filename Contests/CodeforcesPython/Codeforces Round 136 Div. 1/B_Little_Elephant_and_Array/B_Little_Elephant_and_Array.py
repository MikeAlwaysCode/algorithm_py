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
    n, m = mint()
    nums = ints()

    # 提前读入所有查询，按r保存，进行离线求解
    qry = [[] for _ in range(n)]
    for i in range(m):
        l, r = mint()
        qry[r - 1].append((l - 1, i))

    # 树状数组进行区间查询
    bit = [0] * (n + 1)

    def lowbit(x: int) -> int:
        return x & -x

    def query(x: int) -> int:
        ans = 0
        while x:
            ans += bit[x]
            x -= lowbit(x)
        return ans

    def add(x: int, val: int):
        while x <= n:
            bit[x] += val
            x += lowbit(x)

    # 询问的结果
    ans = [0] * m
    pos = defaultdict(list)
    
    for r, x in enumerate(nums):
        pos[x].append(r)
        l = len(pos[x])
        if l >= x:
            # 前x个位置 + 1
            add(pos[x][l - x] + 1, 1)
        if l > x:
            # 前x + 1个位置 - 2， 把前面的1抹除并把前x个位置的1抵消
            add(pos[x][l - x - 1] + 1, -2)
        if l > x + 1:
            # 前x + 2个位置 + 1，把之前x+1位置抵消的1抹除
            add(pos[x][l - x - 2] + 1, 1)
        if not qry[r]: continue
        rs = query(r + 1)
        for l, i in qry[r]:
            ans[i] = rs - query(l)
    
    for v in ans:
        print(v)

solve()