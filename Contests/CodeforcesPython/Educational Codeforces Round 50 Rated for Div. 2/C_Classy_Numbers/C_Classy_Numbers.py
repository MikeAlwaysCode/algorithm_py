import sys
import math

# from functools import cache

# import os
# import random
# from bisect import bisect, bisect_left
# from collections import *
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

pw = [1, 9, 81, 729]

def solve() -> None:
    l, r = mint()

    def f(n: int, m: int) -> int:
        return sum(math.comb(n, i) * pw[i] for i in range(m + 1))

    def zz(s: int) -> int:
        s = str(s)
        res, cnt = 0, 3
        n = len(s)
        for i in range(n):
            if s[i] == '0': continue
            # 当前位填0
            res += f(n - i - 1, cnt)
            cnt -= 1
            if cnt < 0: break
            # 当前位填其他k - 1个数
            res += f(n - i - 1, cnt) * (int(s[i]) - 1)
        return res
    
    print(zz(r + 1) - zz(l))

    '''
    @cache
    def f(i: int, s: str, cnt: int, isLimit: bool, isNum: bool) -> int:
        if i == len(s):
            # 前面填了数字，当前为1个有效结果
            return int(isNum and cnt <= 3)
        if cnt > 3:
            return 0
        res = 0
        if not isNum:
            # 可继续跳过
            res = f(i+1, s, cnt, False, False)
        up = int(s[i]) if isLimit else 9
        for d in range(1-int(isNum), up+1):
            res += f(i+1, s, cnt + int(d > 0), isLimit and d == up, True)
        return res

    print(f(0, str(r), 0, True, False) - f(0, str(l - 1), 0, True, False))
    '''

# sys.setrecursionlimit(100000)
for _ in range(int(input())):
    solve()