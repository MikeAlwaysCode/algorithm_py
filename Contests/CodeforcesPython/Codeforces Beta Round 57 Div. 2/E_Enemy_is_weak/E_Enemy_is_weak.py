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

# Segment tree
# 区间修改，单点查询 4929 ms
# 单点修改，区间查询 TLE
class SegTree:
    def __init__(self, n: int) -> None:
        self.n = n
        self.tree = [0] * (4 * n)
    
    def do(self, o: int, val: int) -> None:
        self.tree[o] += val

    def pushUp(self, o: int) -> None:
        self.tree[o] = self.tree[o * 2] + self.tree[o * 2 + 1]
    
    def update(self, o: int, l: int, r: int, L: int, R: int, val: int) -> None:
        if L <= l and r <= R:
            self.do(o, val)
            return
        
        m = (l + r) >> 1
        if m >= L:
            self.update(o * 2, l, m, L, R, val)
        if m < R:
            self.update(o * 2 + 1, m + 1, r, L, R, val)

        self.pushUp(o)
    
    def query(self, o: int, l: int, r: int, L: int, R: int) -> int:
        if R < l or L > r:
            return 0
        
        if L <= l and r <= R:
            return self.tree[o]
        
        m = (l + r) >> 1
        # 单点修改区间查询，完全包含的区间才累加
        res = 0
        # # 区间修改单点查询，经过的所有区间累加
        # res = self.tree[o]
        if m >= L:
            res += self.query(o * 2, l, m, L, R)
        if m < R:
            res += self.query(o * 2 + 1, m + 1, r, L, R)
        
        return res

def solve() -> None:
    n = sint()
    nums = ints()

    # 序列化
    discretization = {v:i for i, v in enumerate(sorted(nums), 1)}
    ans = 0
    st = SegTree(n)
    for i, x in enumerate(nums):
        x = discretization[x]
        # # 区间修改，单点查询 4929 ms
        # gt = st.query(1, 1, n, x, x)
        # lt = x - 1 - i + gt
        # ans += gt * lt
        # st.update(1, 1, n, 1, x, 1)
        # 单点修改，区间查询
        lt = st.query(1, 1, n, 1, x)
        gt = i - lt
        lt = x - 1 - lt
        ans += gt * lt
        st.update(1, 1, n, x, x, 1)
    
    print(ans)

solve()