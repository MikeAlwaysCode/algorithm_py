import math
import sys

# import itertools
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

class SparseTable:
    def __init__(self, nums: list, op) -> None:
        self.pow2 = [1]
        for _ in range(20):
            self.pow2.append(2 * self.pow2[-1])
        self.op = op
        self.st = []
        s, l = nums, 1
        self.st.append(s)
        while l * 2 <= len(nums):
            ns = []
            for i in range(len(s) - l):
                ns.append(math.gcd(s[i], s[i + l]))
            s = ns
            self.st.append(s)
            l *= 2

    def query(self, l: int, r: int):
        # s = log2(r - l + 1)
        s = len(bin(r - l + 1)) - 3
        res = self.op(self.st[s][l], self.st[s][r - self.pow2[s] + 1])
        return res

def solve() -> None:
    n = sint()
    nums = ints()
    d = list(abs(nums[i] - nums[i - 1]) for i in range(1, n)) + [1]

    ans = 1
    stk = [(-1, 1)]
    for i, x in enumerate(d):
        j, g = i, x
        nstk = []
        for k, pg in stk:
            ng = math.gcd(pg, g)
            if ng != g:
                nstk.append((j, g))
                j, g = k, ng
        nstk.append((j, g))
        stk = nstk
        ans = max(ans, i - stk[-1][0] + 1)

    '''
    # ST + Binary Search 1231ms
    d = list(abs(nums[i] - nums[i - 1]) for i in range(1, n)) + [1]
    # print(d)
    st = SparseTable(d, math.gcd)

    def binary_search(i: int, l: int, r: int) -> int:
        while l < r:
            m = (l + r + 1) // 2
            if st.query(i, m) > 1:
                l = m
            else:
                r = m - 1
        return l

    ans = 1
    for i in range(n - 1):
        if d[i] == 1: continue
        j = binary_search(i, i, n)
        ans = max(ans, j - i + 2)
    '''

    print(ans)

for _ in range(int(input())):
    solve()