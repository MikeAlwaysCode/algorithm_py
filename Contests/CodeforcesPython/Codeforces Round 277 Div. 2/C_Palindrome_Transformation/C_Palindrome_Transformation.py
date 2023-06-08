import math
import sys
from bisect import *
from collections import *
from functools import *
from heapq import *
from itertools import *
from random import *
from string import *
from types import GeneratorType

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
    n, p = mint()
    p -= 1
    s = input()
    ans = 0
    if p * 2 < n:
        l, r = 0, (n + 1) // 2
    else:
        l, r = (n + 1) // 2, n
    
    left = right = -1
    for i in range(l, r):
        if s[i] != s[n - 1 - i]:
            diff = abs(ord(s[i]) - ord(s[n - 1 - i]))
            ans += min(diff, 26 - diff)
            if left == -1: left = i
            right = i
    # print(p, left, right)
    if left != -1:
        if p <= left:
            ans += right - p
        elif p >= right:
            ans += p - left
        else:
            ans += right - left + min(right - p, p - left)

    print(ans)


# for _ in range(int(input())):
solve()