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

    sb = []
    for _ in range(sint()):
        x, y = mint()
        sb.append((x, y))

    # n += 1
    # m += 1
    # g = [[0] * m for _ in range(n)]
    # for _ in range(sint()):
    #     x, y = mint()
    #     g[x][y] = 1
    # # print(g)
    # prefix = [[0] * (m + 1) for _ in range(n + 1)]
    # for i in range(1, n + 1):
    #     for j in range(1, m + 1):
    #         prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + g[i - 1][j - 1]
    # # print(prefix)
    A = sint()
    xs = ints() + [n]
    B = sint()
    ys = ints() + [m]
    # for i in range(A + 1):
    #     x1, x2 = xs[i], xs[i + 1] + 1
    #     for j in range(B + 1):
    #         y1, y2 = ys[j], ys[j + 1] + 1
    #         cnt = prefix[x2][y2] - prefix[x1][y2] - prefix[x2][y1] + prefix[x1][y1]
    #         mn = min(mn, cnt)
    #         mx = max(mx, cnt)         
    xsb = []
    sb.sort()
    i = 0
    for x, y in sb:
        while xs[i] < x:
            i += 1
        xsb.append((i, y))
    xsb.sort(key = lambda x: x[1])
    nsb = []
    i = 0
    for x, y in xsb:
        while ys[i] < y:
            i += 1
        nsb.append((x, i))
    nsb.sort()
    # print(nsb)

    mn, mx = math.inf, 0
    cnt = 0
    px = py = -1
    for i, (x, y) in enumerate(nsb):
        if x != px:
            if x - px > 1 or y > 0:
                mn = 0
            if px != -1:
                mn = min(mn, cnt)
                mx = max(mx, cnt)
            cnt = 1
            px = x
            py = y
        elif y != py:
            if y - py > 1:
                mn = 0
            mn = min(mn, cnt)
            mx = max(mx, cnt)
            py = y
            cnt = 1
        else:
            cnt += 1
            mn = min(mn, cnt)
            mx = max(mx, cnt)
        
    mn = min(mn, cnt)
    mx = max(mx, cnt)

    print(mn, mx)

solve()