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
    perm = []
    for _ in range(m):
        perm.append(ints())

    pos = [0] * n
    for i in range(n):
        pos[perm[0][i] - 1] = i
    
    mn = [n] * n
    
    for i in range(m):
        dp = [1] * n
        for j in range(n - 1, -1, -1):
            perm[i][j] = pos[perm[i][j] - 1]
            if j < n - 1 and perm[i][j] == perm[i][j + 1] - 1:
                dp[j] = dp[j + 1] + 1
            mn[perm[i][j]] = min(mn[perm[i][j]], dp[j])
            
    ans = cur = 0
    while cur < n:
        ans += mn[cur] * (mn[cur] + 1) // 2
        cur += mn[cur]

    '''
    for i in range(m):
        for j in range(n):
            perm[i][j] = pos[perm[i][j] - 1]
    
    mn = [n] * n
    for i in range(m):
        cur = 0
        for j in range(n):
            if cur < j: cur += 1
            while cur < n - 1 and perm[i][cur + 1] == perm[i][cur] + 1:
                cur += 1
            mn[perm[i][j]] = min(mn[perm[i][j]], perm[i][cur])
    
    ans = cur = 0
    while cur < n:
        l = mn[cur] - cur + 1
        ans += l * (l + 1) // 2
        cur = mn[cur] + 1
    '''

    print(ans)

# for _ in range(int(input())):
solve()