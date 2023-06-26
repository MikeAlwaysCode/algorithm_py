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
    h = [0] * 3
    w = [0] * 3
    g = [[] for _ in range(3)]
    for i in range(3):
        h[i], w[i] = mint()
        for _ in range(h[i]):
            g[i].append(input())
    
    cnt = [0] * 2
    for k in range(2):
        res = 0
        for i in range(h[k]):
            for j in range(w[k]):
                if g[k][i][j] == "#":
                    res += 1
        cnt[k] = res
    
    def check(i0: int, j0: int, i1: int, j1: int) -> bool:
        b0 = b1 = 0
        for i in range(h[2]):
            for j in range(w[2]):
                c = "."
                if 0 <= i - i0 < h[0] and 0 <= j - j0 < w[0] and g[0][i - i0][j - j0] == "#":
                    c = "#"
                    b0 += 1
                if 0 <= i - i1 < h[1] and 0 <= j - j1 < w[1] and g[1][i - i1][j - j1] == "#":
                    c = "#"
                    b1 += 1
                if c != g[2][i][j]:
                    return False
        return b0 == cnt[0] and b1 == cnt[1]
    
    for i0 in range(- h[0], h[2] + 1):
        for j0 in range(- w[0], w[2] + 1):
            for i1 in range(- h[1], h[2] + 1):
                for j1 in range(- w[1], w[2] + 1):
                    if check(i0, j0, i1, j1):
                        print("Yes")
                        return
    
    print("No")

solve()