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

# 通过前缀函数求最长前缀回文串
def find_palindrome(s: str) -> int:
    s = s + "#" + s[::-1]
    n = len(s)
    pref = [0] * n
    k = 0
    for i in range(1, n):
        while k and s[k] != s[i]:
            k = pref[k - 1]
        if s[k] == s[i]: k += 1
        pref[i] = k
    return pref[-1]


def solve() -> None:
    s = input()
    n, l = len(s), 0
    while l * 2 <= n - 2 and s[l] == s[n - l - 1]:
        l += 1
    # ans = s[:l]
    m = ""
    if l * 2 < n:
        mid = s[l:n - l]
        a = find_palindrome(mid)
        b = find_palindrome(mid[::-1])
        if a >= b:
            # ans += mid[:a]
            m = mid[:a]
        else:
            # ans += mid[-b:]
            m = mid[-b:]
    # ans += s[n - l:]
    # print(ans)
    print(s[:l] + m + s[n - l:])

for _ in range(int(input())):
    solve()