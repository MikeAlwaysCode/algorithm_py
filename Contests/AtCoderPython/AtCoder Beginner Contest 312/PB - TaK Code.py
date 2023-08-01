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
    n, m = mint()
    g = []
    for _ in range(n):
        g.append(input())
    
    def check(x: int, y: int) -> bool:
        if x + 8 >= n or y + 8 >= m: return False
        for i in range(x, x + 3):
            for j in range(y, y + 3):
                if g[i][j] != "#": return False
        for i in range(x + 6, x + 9):
            for j in range(y + 6, y + 9):
                if g[i][j] != "#": return False
        for i in range(x, x + 4):
            if g[i][y + 3] != ".": return False
        for i in range(x + 5, x + 9):
            if g[i][y + 5] != ".": return False
        for j in range(y, y + 4):
            if g[x + 3][j] != ".": return False
        for j in range(y + 5, y + 9):
            if g[x + 5][j] != ".": return False
        return True

    for i in range(n):
        for j in range(m):
            if check(i, j): print(i + 1, j + 1)

solve()