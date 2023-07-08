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

class BIT:
    def __init__(self, n: int):
        self.nums = [0] * (n + 1)
        self.n = n
        self.BITree = [0] * (self.n + 1)
        
    def lowbit(self, x: int) -> int:
        return x & -x
    
    def query(self, x: int) -> int:
        ans = 0
        while x:
            ans += self.BITree[x]
            x -= self.lowbit(x)
        return ans

    def add(self, x: int, val: int):
        while x <= self.n:
            self.BITree[x] += val
            x += self.lowbit(x)

    def update(self, x: int, val: int) -> None:
        self.add(x + 1, val - self.nums[x])
        self.nums[x] = val

def solve() -> None:
    n, m, q = mint()
    nums = [0] + list(map(int, list(input())))
    s = sum(nums)
    nxt = list(range(n + 1))
    p = []
    for _ in range(m):
        l, r = mint()
        while l <= r:
            while l <= n and l != nxt[l]:
                l = nxt[l]
            if l <= r:
                p.append(l)
                nxt[l] = r + 1
                l += 1
    k = len(p)
    for i in range(1, n + 1):
        if nxt[i] == i: p.append(i)
    # print(p)
    d = [0] * (n + 1)
    bt = BIT(n + 1)
    for i, v in enumerate(p, 1):
        d[v] = i
        if nums[v] == 0: bt.update(i, 1)
    # print(d)
    for _ in range(q):
        x = sint()
        s -= nums[x]
        nums[x] ^= 1
        s += nums[x]
        bt.update(d[x], nums[x] ^ 1)
        print(bt.query(min(k, s) + 1))

solve()

