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

class SegTree:
    def __init__(self, n: int) -> None:
        self.n = n
        self.tree = [0] * (4 * n)
        self.lazy = [0] * (4 * n)
    
    def do(self, o: int, l: int, r: int, val: int) -> None:
        self.tree[o] += (r - l + 1) * val
        self.lazy[o] += val
    
    def pushUp(self, o: int) -> None:
        self.tree[o] = self.tree[o * 2] + self.tree[o * 2 + 1]
    
    def pushDown(self, o: int, l: int, r: int) -> None:
        m = (l + r) >> 1
        self.do(o * 2, l, m, self.lazy[o])
        self.do(o * 2 + 1, m + 1, r, self.lazy[o])
        self.lazy[o] = 0
    
    def update(self, o: int, l: int, r: int, L: int, R: int, val: int) -> None:
        if L <= l and R >= r:
            self.do(o, l, r, val)
            return

        if self.lazy[o]:
            self.pushDown(o, l, r)
        
        m = (l + r) >> 1
        if m >= L:
            self.update(o * 2, l, m, L, R, val)
        if m < R:
            self.update(o * 2 + 1, m + 1, r, L, R, val)
        
        self.pushUp(o)
    
    def query(self, o: int, l: int, r: int, L: int, R: int) -> int:
        if R < l or L > r:
            return 0

        if L <= l and R >= r:
            return self.tree[o]
        
        if self.lazy[o]:
            self.pushDown(o, l, r)
        
        m = (l + r) >> 1
        res = 0
        if m >= L:
            res += self.query(o * 2, l, m, L, R)
        if m < R:
            res += self.query(o * 2 + 1, m + 1, r, L, R)
        
        return res

class BIT:
    def __init__(self, n: int):
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

def solve() -> None:
    n = sint()
    nums = ints()
    
    # st = SegTree(n)
    bit = BIT(n)

    discretization = {v:i for i, v in enumerate(sorted(nums), 1)}
    lcnt = Counter(discretization[v] for v in nums)
    rcnt = Counter()
    ans = 0
    for i in range(n - 1, -1, -1):
        d = discretization[nums[i]]

        # ans += st.query(1, 1, n, 1, lcnt[d] - 1)
        ans += bit.query(lcnt[d])

        lcnt[d] -= 1
        rcnt[d] += 1

        # st.update(1, 1, n, rcnt[d], rcnt[d], 1)
        bit.add(rcnt[d] + 1, 1)
    
    print(ans)

solve()