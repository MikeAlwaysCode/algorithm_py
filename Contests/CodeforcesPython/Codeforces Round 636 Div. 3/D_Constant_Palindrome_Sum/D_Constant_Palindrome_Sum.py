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
    n, k = mint()
    nums = ints()
    cnt = [0] * (k * 2 + 2)
    for i in range(n // 2):
        j = n - i - 1
        s = nums[i] + nums[j]
        # l = min(nums[i], nums[n - i - 1]) + 1
        # r = max(nums[i], nums[n - i - 1]) + k
        if nums[i] > nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        l = nums[i] + 1
        r = nums[j] + k
        cnt[2] += 2
        cnt[l] -= 1
        cnt[s] -= 1
        cnt[s + 1] += 1
        cnt[r + 1] += 1

    ans = math.inf
    cost = 0
    for i in range(2, k * 2 + 1):
        cost += cnt[i]
        # ans = min(ans, cost)
        if cost < ans: ans = cost
    print(ans)

for _ in range(int(input())):
    solve()