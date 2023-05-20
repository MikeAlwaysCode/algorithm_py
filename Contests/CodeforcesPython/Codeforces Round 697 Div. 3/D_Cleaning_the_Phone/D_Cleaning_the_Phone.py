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
    A = ints()
    B = ints()
    
    arr = [[] for _ in range(2)]
    s = 0
    for a, b in zip(A, B):
        arr[b-1].append(a)
        s += a
    
    if s < m:
        print(-1)
        return
        
    arr[0].sort(reverse=True)
    arr[1].sort(reverse=True)
        
    ans = math.inf
    s = i = j = 0
    while i < len(arr[0]) and s < m:
        s += arr[0][i]
        i += 1
    if s >= m: ans = i

    while j < len(arr[1]):
        s += arr[1][j]
        j += 1
        while i > 0 and s - arr[0][i - 1] >= m:
            s -= arr[0][i - 1]
            i -= 1
        if s >= m: ans = min(ans, i + j * 2)
        

    print(ans)

for _ in range(int(input())):
    solve()