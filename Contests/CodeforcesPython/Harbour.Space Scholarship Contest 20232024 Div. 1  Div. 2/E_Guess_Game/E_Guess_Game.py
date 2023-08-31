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

MOD = 998244353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

class BinaryTrie:
    def __init__(self, max_bit: int = 30):
        self.inf = 1 << 63
        self.to = [[-1], [-1]]
        self.cnt = [0]
        self.max_bit = max_bit

    def add(self, num: int) -> None:
        cur = 0
        self.cnt[cur] += 1
        for k in range(self.max_bit, -1, -1):
            bit = (num >> k) & 1
            if self.to[bit][cur] == -1:
                self.to[bit][cur] = len(self.cnt)
                self.to[0].append(-1)
                self.to[1].append(-1)
                self.cnt.append(0)
            cur = self.to[bit][cur]
            self.cnt[cur] += 1

    def count(self, cur: int, k: int) -> int:
        res = 0
        bit = k + 1

        if self.to[0][cur] != -1 and self.to[1][cur] != -1:
            # 后续两个分支都有节点，计算a != b的情况
            # a < b: 如果第k位是a猜，a知道是a < b, 如果第k位是b猜，b不知道答案，要下一轮a猜和知道答案
            res += (bit + (bit & 1 ^ 1)) * self.cnt[self.to[0][cur]] * self.cnt[self.to[1][cur]]
            # a > b: 如果第k位是a猜，a不知道答案，需要下一轮B猜, 如果第k位是b猜，b知道a > b
            res += (bit + (bit & 1)) * self.cnt[self.to[0][cur]] * self.cnt[self.to[1][cur]]

        if self.to[0][cur] == -1 and self.to[1][cur] == -1:
            # 已经是最后的分支节点，计算a == b的情况
            res += bit * self.cnt[cur] * self.cnt[cur]

        if self.to[0][cur] != -1:
            # 从第1位不是0的开始猜，相当于起始位不变
            res += self.count(self.to[0][cur], k)
        
        if self.to[1][cur] != -1:
            # 需要从高位含1的开始猜，k + 1
            res += self.count(self.to[1][cur], k + 1)

        return res

def solve() -> None:
    n = sint()
    nums = ints()
    bt = BinaryTrie()
    for x in nums:
        bt.add(x)
    ans = bt.count(0, 0)
    rev = pow(n, MOD - 2, MOD)
    ans = ans * rev % MOD * rev % MOD
    print(ans)

for _ in range(int(input())):
    solve()