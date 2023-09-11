import math
import sys
from itertools import *

# from bisect import *
# from collections import *
# from functools import *
# from heapq import *
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
    g = []
    for _ in range(3):
        g.append(ints())
    
    q = p = 0
    for per in permutations(range(9)):
        row = [[] for _ in range(3)]
        col = [[] for _ in range(3)]
        dia1 = []
        dia2 = []
        check = True
        for x in per:
            r, c = divmod(x, 3)
            row[r].append(g[r][c])
            col[c].append(g[r][c])
            if r == c:
                dia1.append(g[r][c])
            if r + c == 2:
                dia2.append(g[r][c])
            if len(row[r]) >= 2 and row[r][0] == row[r][1]:
                check = False
                break
            if len(col[c]) >= 2 and col[c][0] == col[c][1]:
                check = False
                break
            if len(dia1) >= 2 and dia1[0] == dia1[1]:
                check = False
                break
            if len(dia2) >= 2 and dia2[0] == dia2[1]:
                check = False
                break
        if check: p += 1
        q += 1

    print(p / q)

solve()