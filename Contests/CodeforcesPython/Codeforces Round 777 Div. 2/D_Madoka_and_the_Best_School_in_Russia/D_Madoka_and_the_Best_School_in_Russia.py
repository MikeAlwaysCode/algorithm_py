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

def solve() -> None:
    x, d = mint()

    cnt_d = 0
    while x % d == 0:
        x //= d
        cnt_d += 1

    # 1. 只有一个d，只能有一种表示
    if cnt_d < 2:
        print("NO")
        return
    
    cnt = 0
    p = 2
    while p * p <= x:
        while x % p == 0:
            x //= p
            cnt += 1
        if x == 1: break
        p += 1
    if x > 1: cnt += 1

    if cnt >= 2:
        # 2. 有两个以上与d无关的质因子，随意组合分配即可
        print("YES")
    elif cnt_d == 2:
        # 3. 只有两个d，一个无关的质因子，分配给哪个都一样
        print("NO")
    elif cnt == 1 and d == x * x:
        # 4. 只有一个质因子p，且d为p的平方，若把一个d分解后，有三个p，此时若d的个数仍大于等于3，可以有两种表示d*d*d*d*p / d*p * d*p * d*p 
        print("YES" if cnt_d > 3 else "NO")
    else:
        # 5. 若能把一个d分解成其他质因子，则有其他表示
        cnt_d -= 1
        p = 2
        x = d
        while p * p <= x:
            while x % p == 0:
                x //= p
                cnt += 1
            if x == 1: break
            p += 1
        if x > 1 and x != d: cnt += 1
        elif x == d: cnt_d += 1
        print("YES" if cnt >= 2 else "NO")
    

for _ in range(int(input())):
    solve()