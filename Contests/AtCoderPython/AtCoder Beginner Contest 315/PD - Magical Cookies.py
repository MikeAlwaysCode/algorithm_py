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
    n, m = mint()
    row = [[0] * 26 for _ in range(n)]
    col = [[0] * 26 for _ in range(m)]
    g = []
    for i in range(n):
        g.append(input())
        for j, c in enumerate(g[-1]):
            d = ord(c) - 97
            row[i][d] += 1
            col[j][d] += 1
    ans = n * m
    rcnt, ccnt = m, n
    row_del = [False] * n
    col_del = [False] * m
    row_del_c = [0] * 26
    col_del_c = [0] * 26
    while True:
        check = False
        new_rcnt, new_ccnt = rcnt, ccnt
        new_row_del_c = row_del_c[:]
        new_col_del_c = col_del_c[:]
        j = 0
        while j < m and col_del[j]:
            j += 1
        if j < m:
            for i in range(n):
                if row_del[i]: continue
                d = ord(g[i][j]) - 97
                if rcnt > 1 and row[i][d] - col_del_c[d] == rcnt:
                    ans -= new_rcnt
                    new_ccnt -= 1
                    row_del[i] = True
                    check = True
                    new_row_del_c[d] += 1
        i = 0
        while i < n and row_del[i]:
            i += 1
        if i < n:
            for j in range(m):
                if col_del[j]: continue
                d = ord(g[i][j]) - 97
                if ccnt > 1 and col[j][d] - row_del_c[d] == ccnt:
                    ans -= new_ccnt
                    new_rcnt -= 1
                    col_del[j] = True
                    check = True
                    new_col_del_c[d] += 1

        if not check: break
        rcnt, ccnt = new_rcnt, new_ccnt
        row_del_c = new_row_del_c
        col_del_c = new_col_del_c

    print(ans)

solve()