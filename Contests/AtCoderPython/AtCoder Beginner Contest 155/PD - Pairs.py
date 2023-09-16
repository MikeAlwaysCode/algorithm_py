import math
import sys
from bisect import *

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
    n, k = mint()
    nums = ints()
    nums.sort()

    p = bisect_left(nums, 0)
    q = bisect_left(nums, 1)
    
    neg = p * (n - q)
    if k <= neg:
        k = neg - k + 1

        def zz1(x: int) -> bool:
            res = 0
            j = q
            for a in nums[:p]:
                a = -a
                while j < n and nums[j] * a <= x:
                    j += 1
                res += j - q 
            return res
        
        print(-bisect_left(range(10 ** 18 + 1), k, key = zz1))
        return
    
    k -= neg
    c0 = q - p
    zero = c0 * (n - c0) + c0 * (c0 - 1) // 2
    if k <= zero:
        print(0)
        return

    k -= zero
    
    def zz2(x: int) -> bool:
        res = 0
        i, j = 0, p - 1
        while i < j:
            if nums[i] * nums[j] > x:
                i += 1
            else:
                res += j - i
                j -= 1
        i, j = q, n - 1
        while i < j:
            if nums[i] * nums[j] > x:
                j -= 1
            else:
                res += j - i
                i += 1
                
        return res
    
    print(bisect_left(range(10 ** 18 + 1), k, key = zz2))

solve()