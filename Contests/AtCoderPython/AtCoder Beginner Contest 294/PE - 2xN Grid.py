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
    L, n1, n2 = mint()
    A = []
    B = []
    for _ in range(n1):
        A.append(list(mint()))
    for _ in range(n2):
        B.append(list(mint()))

    ans = 0
    i = j = 0
    while i < n1 and j < n2:
        if A[i][0] == B[j][0]:
            ans += min(A[i][1], B[j][1])
        if A[i][1] > B[j][1]:
            A[i][1] -= B[j][1]
            j += 1
        else:
            B[j][1] -= A[i][1]
            i += 1

    '''
    i = j = 1
    l1, r1, v1 = 1, A[0][1], A[0][0]
    l2, r2, v2 = 1, B[0][1], B[0][0]
    
    while i < n1 or j < n2:
        if v1 == v2:
            r = min(r1, r2)
            l = max(l1, l2)
            ans += max(0, r - l + 1)

        if r1 > r2:
            l2, r2, v2 = r2 + 1, r2 + B[j][1], B[j][0]
            j += 1
        elif r2 > r1:
            l1, r1, v1 = r1 + 1, r1 + A[i][1], A[i][0]
            i += 1
        else:
            l1, r1, v1 = r1 + 1, r1 + A[i][1], A[i][0]
            i += 1
            l2, r2, v2 = r2 + 1, r2 + B[j][1], B[j][0]
            j += 1
    if v1 == v2:
        r = min(r1, r2)
        l = max(l1, l2)
        ans += max(0, r - l + 1)
    '''

    print(ans)

solve()