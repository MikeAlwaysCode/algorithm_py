import sys
from sortedcontainers import sortedlist

# import math
# import os
# import random
# from bisect import bisect, bisect_left
# from collections import *
# from functools import reduce
# from heapq import heapify, heappop, heappush
# from itertools import *
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

# MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR4 = ((-1, 0), (0, 1), (1, 0), (0, -1)) #URDL
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

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
    n, m = mint()
    s = list(ord(x) - 97 for x in input())
    ss2 = sortedlist()
    # print(s)
    bit_left2 = BIT(n)
    bit_right2 = BIT(n)
    bit_left3 = BIT(n)
    bit_right3 = BIT(n)
    bit_op = BIT(n + 1)
    for i in range(1, n):
        if s[i] == s[i - 1]:
            bit_left2.add(i, 1)
            bit_right2.add(i + 1, 1)
        if i > 1 and s[i] == s[i - 2]:
            bit_left3.add(i - 1, 1)
            bit_right3.add(i + 1, 1)
    
    op = [0] * n
    for _ in range(m):
        qry = ints()
        if qry[0] == 1:
            l, r, x = qry[1:]
            for i in range(max(1, l - 2), min(r, l + 1) + 1):
                op[i - 1] = bit_op.query(i)
            for i in range(max(l + 2, r - 1), min(n, r + 2) + 1):
                op[i - 1] = bit_op.query(i)

            if l > 1 and (s[l - 1] + op[l - 1]) % 26 == (s[l - 2] + op[l - 2]) % 26:
                bit_left2.add(l - 1, -1)
                bit_right2.add(l, -1)
                    
            if l > 1 and (s[l - 1] + op[l - 1] + x) % 26 == (s[l - 2] + op[l - 2]) % 26:
                bit_left2.add(l - 1, 1)
                bit_right2.add(l, 1)

            for i in range(l, min(r, l + 1) + 1):
                if i > 2 and (s[i - 1] + op[i - 1]) % 26 == (s[i - 3] + op[i - 3]) % 26:
                    bit_left3.add(i - 2, -1)
                    bit_right3.add(i, -1)
                    
                if i > 2 and (s[i - 1] + op[i - 1] + x) % 26 == (s[i - 3] + op[i - 3]) % 26:
                    bit_left3.add(i - 2, 1)
                    bit_right3.add(i, 1)

            if r > l and (s[r - 1] + op[r - 1]) % 26 == (s[r - 2] + op[r - 2]) % 26:
                bit_left2.add(r - 1, -1)
                bit_right2.add(r, -1)

            if r > l and (s[r - 1] + op[r - 1]) % 26 == (s[r - 2] + op[r - 2] + x) % 26:
                bit_left2.add(r - 1, 1)
                bit_right2.add(r, 1)

            for i in range(max(l + 2, r + 1), min(n, r + 2) + 1):
                if i > 2 and (s[i - 1] + op[i - 1]) % 26 == (s[i - 3] + op[i - 3]) % 26:
                    bit_left3.add(i - 2, -1)
                    bit_right3.add(i, -1)

                if i > 2 and (s[i - 1] + op[i - 1]) % 26 == (s[i - 3] + op[i - 3] + x) % 26:
                    bit_left3.add(i - 2, 1)
                    bit_right3.add(i, 1)

            bit_op.add(l, x)
            bit_op.add(r + 1, -x)
        else:
            l, r = qry[1:]
            lcnt2 = bit_left2.query(l - 1)
            rcnt2 = bit_right2.query(r)
            lcnt3 = bit_left3.query(l - 1)
            rcnt3 = bit_right3.query(r)
            print("NO" if rcnt2 > lcnt2 or rcnt3 > lcnt3 else "YES")

for _ in range(int(input())):
    solve()