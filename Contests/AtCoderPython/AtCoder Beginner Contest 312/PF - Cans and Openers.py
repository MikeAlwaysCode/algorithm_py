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
    nums = [[] for _ in range(3)]
    for _ in range(n):
        t, x = mint()
        nums[t].append(x)
    
    pres = []
    for i in range(3):
        nums[i].sort(reverse = True)
        # pres.append(list(accumulate(nums[i], initial = 0)))
        pres.append([0] + list(accumulate(nums[i])))
    
    comb = []
    j = 0
    for i in range(len(pres[1])):
        while j < len(pres[2]) and pres[2][j] < i:
            j += 1
        if j >= len(pres[2]) or i + j > m: break
        comb.append((i + j, pres[1][i]))
    ans = 0
    for i in range(len(pres[0])):
        # j = bisect(comb, m - i, key = lambda x: x[0])
        if i > m: break
        j = bisect(comb, (m - i, math.inf))
        ans = max(ans, pres[0][i] + comb[j - 1][1])

    print(ans)

solve()