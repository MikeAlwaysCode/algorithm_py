import sys
import math

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
    n = sint()
    p = []
    for _ in range(n):
        p.append(tuple(mint()))
    
    A = p[-1][1] - p[0][1]
    B = p[0][0] - p[-1][0]
    C = (p[0][1] - p[-1][1]) * p[0][0] + (p[-1][0] - p[0][0]) * p[0][1]
    d = []
    for i in range(1, n - 1):
        dis = abs(A * p[i][0] + B * p[i][1] + C) / math.sqrt(A * A + B * B)
        d.append((dis, i))
    skip = [False] * n
    cost, c = 1, 0
    d.sort(reverse = True)
    print(d)
    for dis, i in d:
        if dis >= cost:
            skip[i] = True
            c += 1
            cost = pow(2, c) - cost
    ans = 0.0
    px, py = p[0][0], p[0][1]
    for i in range(1, n):
        if skip[i]: continue
        ans += math.sqrt(pow(abs(p[i][0] - px), 2) + pow(abs(p[i][1] - py), 2))
        px, py = p[i][0], p[i][1]
    print(ans)

solve()