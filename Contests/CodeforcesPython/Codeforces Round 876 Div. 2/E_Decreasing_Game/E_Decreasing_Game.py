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
    nums = [0] + ints()
    s = sum(nums)
    # 01背包
    target = s // 2
    dp = [0] * (s + 1)
    if not s & 1:
        dp[0] = 1
        for i, x in enumerate(nums[1:], 1):
            for j in range(target, x - 1, -1):
                if dp[j] == 0 and dp[j - x]:
                    dp[j] = i
    if s & 1 or not dp[target]: # 无法均分，先手必胜
        print("First", flush = True)
        si = set(range(1, n + 1))
        while True:
            x = si.pop()
            print(x, flush = True)
            y = sint()
            if not y: break
            si.remove(y)
            mn = min(nums[x], nums[y])
            nums[x] -= mn
            nums[y] -= mn
            if nums[x]: si.add(x)
            if nums[y]: si.add(y)
    else:
        si = [set(), set()]  # 构成target分两部分
        while target:
            si[0].add(dp[target])
            target -= nums[dp[target]]
        for i in range(1, n + 1):
            if i not in si[0]: si[1].add(i)
        print("Second", flush = True)
        while True:
            x = sint()
            if not x: break
            i = 1 if x in si[0] else 0
            si[i^1].remove(x)
            y = si[i].pop()
            mn = min(nums[x], nums[y])
            nums[x] -= mn
            nums[y] -= mn
            if nums[x]: si[i^1].add(x)
            if nums[y]: si[i].add(y)
            
            print(y, flush = True)
        

# for _ in range(int(input())):
solve()