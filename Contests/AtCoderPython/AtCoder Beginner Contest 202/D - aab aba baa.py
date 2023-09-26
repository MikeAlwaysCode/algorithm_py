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
    a, b, k = mint()
    n = a + b
    ans = ['a'] * n
    c = [[0] * (b + 1) for _ in range(n)]
    c[0][0] = c[1][0] = c[1][1] = 1
    for i in range(2, n):
        c[i][0] = 1
        for j in range(1, min(i, b) + 1):
            c[i][j] = c[i - 1][j - 1] + c[i - 1][j]
            
    for i in range(n):
        if k > c[n - i - 1][b]:
            ans[i] = 'b'
            k -= c[n - i - 1][b]
            b -= 1
            if b == 0: break
        else:
            a -= 1
    print("".join(ans))

solve()