# import math
import sys

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
MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def solve() -> None:
    n = sint()
    T = ints()
    A = ints()
    ans = 1
    # 88 ms
    for i in range(n):
        if i == 0 or T[i] > T[i - 1]:
            l = r = T[i]
        else:
            l, r = 1, T[i]
        if i == n - 1 or A[i] > A[i + 1]:
            l = max(l, A[i])
            r = min(r, A[i])
        else:
            r = min(r, A[i])
        if l > r:
            print(0)
            return
        ans = ans * (r - l + 1) % MOD
    '''
    # 90 ms
    l, r = [-math.inf] * n, [math.inf] * n
    l[-1] = r[-1] = A[-1]
    for i in range(n - 2, -1, -1):
        if A[i] > A[i + 1]:
            l[i] = r[i] = A[i]
        else:
            l[i], r[i] = 1, A[i]
    l[0] = max(l[0], T[0])
    r[0] = min(r[0], T[0])
    if l[0] > r[0]:
        print(0)
        return
    ans = 1
    for i in range(1, n):
        if T[i] > T[i - 1]:
            l[i] = max(l[i], T[i])
            r[i] = min(r[i], T[i])
        else:
            l[i] = max(l[i], 1)
            r[i] = min(r[i], T[i])
        if l[i] > r[i]:
            print(0)
            return
        ans = ans * (r[i] - l[i] + 1) % MOD
    '''
    print(ans)

solve()