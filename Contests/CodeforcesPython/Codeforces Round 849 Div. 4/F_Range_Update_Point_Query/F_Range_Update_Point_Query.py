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

'''
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
    n, q = mint()
    nums = ints()
    cnt = [0] * n
    bit = BIT(n)
    for _ in range(q):
        qry = ints()
        if qry[0] == 1:
            bit.add(qry[1], 1)
            bit.add(qry[2] + 1, -1)
        else:
            x = qry[1] - 1
            t = bit.query(x + 1)
            while nums[x] >= 10 and cnt[x] < t:
                nums[x] = sum(map(int, str(nums[x])))
                cnt[x] += 1
            cnt[x] = t
                
            print(nums[x])
'''


def solve() -> None:
    n, q = mint()
    nums = ints()
    
    fa = list(range(n + 1))
    def find(x: int):
        cur = x
        while x != fa[x]:
            x = fa[x]
        while fa[cur] != x:
            fa[cur], cur = x, fa[cur]
        return x

    def union(x: int, y: int):
        fa[find(x)] = find(y)

    for _ in range(q):
        qry = ints()
        if qry[0] == 1:
            x = find(qry[1] - 1)
            while x < qry[2]:
                nums[x] = sum(map(int, str(nums[x])))
                if nums[x] < 10:
                    union(x, x + 1)
                x = find(x + 1)
        else:
            print(nums[qry[1] - 1])

for _ in range(int(input())):
    solve()