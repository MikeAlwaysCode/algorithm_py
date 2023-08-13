import sys
from bisect import bisect_left

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

def f(nums: list, max_bit: int, pre: int):
    if max_bit < 0 or not nums or nums[0] == nums[-1]:
        return 0
    
    bit = 1 << max_bit
    if (nums[0] & bit) == (nums[-1] & bit):
        return f(nums, max_bit - 1, pre | (nums[0] & bit))
    else:
        i = bisect_left(nums, pre | bit)
        return min(f(nums[:i], max_bit - 1, pre), f(nums[i:], max_bit - 1, pre | bit)) | bit

def solve() -> None:
    n = sint()
    nums = ints()
    nums.sort()
    print(f(nums, 29, 0))

solve()