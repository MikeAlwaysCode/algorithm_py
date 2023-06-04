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
    n = sint()
    nums = ints()
    
    ans = [n] * n

    mx = n
    @cache
    def dfs(i, j, x):
        while i < n - 1 and nums[i + 1] > nums[i]:
            i += 1
        while j > 0 and nums[j - 1] < nums[j]:
            j -= 1
        res = j - i

        if j > i and nums[j] > nums[i]: res -= 1
        ans[x] = min(ans[x], x + max(0, res))
        if ans[x] == 3:
            print(i, j, x)
        if res <= 0:
            nonlocal mx
            mx = min(mx, x)
        else:
            dfs(i + 1, j, x + 1)
            dfs(i, j - 1, x + 1)
    dfs(0, n - 1, 0)
    for i in range(mx, n):
        ans[i] = mx
    print(*ans)

for _ in range(int(input())):
    solve()