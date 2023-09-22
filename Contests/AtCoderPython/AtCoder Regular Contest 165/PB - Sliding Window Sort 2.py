import sys

from sortedcontainers import SortedList

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
    n, k = ints()
    nums = ints()
    
    if k == 1:
        print(*nums)
        return
    elif n == k:
        print(*sorted(nums))
        return
    
    pres = [0] * n
    for i in range(1, n):
        pres[i] = pres[i - 1] + (nums[i] > nums[i - 1])
        if i >= k - 1 and pres[i] - pres[i - k + 1] == k - 1:
            print(*nums)
            return
    
    ans = nums[:]
    ss = SortedList()
    for i in range(n - 1, n - k - 1, -1):
        ss.add(nums[i])
    for i in range(n - k - 1, -1, -1):
        ss.remove(nums[i + k])
        if nums[i] > ss[0]:
            ss.add(nums[i + k])
            for j in range(i + 1, i + 1 + k):
                ans[j] = ss[j - i - 1]
            print(*ans)
            return
        ss.add(nums[i])
    for j in range(k):
        ans[j] = ss[j]
    print(*ans)

solve()