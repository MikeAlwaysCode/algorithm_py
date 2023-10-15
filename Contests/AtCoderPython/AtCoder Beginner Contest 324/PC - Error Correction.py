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
    ans = []
    tn = len(t)
    for i in range(1, n + 1):
        s = input()
        sn = len(s)
        if sn == tn:
            cnt = 0
            for j in range(sn):
                if s[j] != t[j]:
                    cnt += 1
            if cnt <= 1: ans.append(i)
        elif sn == tn + 1:
            j, k = 0, tn - 1
            while j < tn and s[j] == t[j]:
                j += 1
            while k >= 0 and t[k] == s[k + 1]:
                k -= 1
            if k < j: ans.append(i)
        elif sn == tn - 1:
            j, k = 0, sn - 1
            while j < sn and s[j] == t[j]:
                j += 1
            while k >= 0 and t[k + 1] == s[k]:
                k -= 1
            if k < j: ans.append(i)

    print(len(ans))
    print(*ans)

solve()