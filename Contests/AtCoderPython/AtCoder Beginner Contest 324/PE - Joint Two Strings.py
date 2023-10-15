import sys

# import math
# from bisect import *
# from collections import *
# from functools import *
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
    n, t = input().split()
    n = int(n)
    tn = len(t)
    cnt = [0] * tn
    ans = 0
    ss = []
    m = 0
    for _ in range(n):
        s = input()
        sn = len(s)
        j = 0
        for i in range(sn):
            if s[i] == t[j]:
                j += 1
                if j >= tn: break
        if j == tn:
            ans += (n - m) * 2 - 1
            m += 1
        else:
            cnt[j] += 1
            ss.append(s)
    for s in ss:
        sn = len(s)
        j = tn - 1
        for i in range(sn - 1, -1, -1):
            if s[i] == t[j]:
                ans += cnt[j]
                j -= 1
                if j < 0: break
    print(ans)

solve()