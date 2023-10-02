import sys
from functools import cache

# import math
# from bisect import *
# from collections import *
# from heapq import *
# from itertools import *
# from random import *
# from string import *
# from types import GeneratorType

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
    n, k = mint()
    s = str(n)

    @cache
    def zz(i: int, mul: int, isLimit: bool, isNum: bool):
        if i == len(s):
            # 前面填了数字，当前为1个有效结果
            return int(isNum and mul <= k)
        if mul == 0:
            if isLimit:
                return int(s[i:]) + 1 if isNum else int(s[i:])
            else:
                return pow(10, len(s) - i)
        res = 0
        if not isNum:
            # 可继续跳过
            res = zz(i+1, mul, False, False)
        up = int(s[i]) if isLimit else 9
        for d in range(1-int(isNum), up+1):
            res += zz(i+1, mul * d, isLimit and d == up, True)
        return res

    print(zz(0, 1, True, False))

sys.setrecursionlimit(10 ** 5)
solve()