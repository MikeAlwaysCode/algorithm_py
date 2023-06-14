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
    m = sint()

    # 单调栈计算切割点的左右边界
    left = [-1] * n
    right = [n] * n
    stk = []
    for i, x in enumerate(nums):
        while stk and x > nums[stk[-1]]:
            right[stk.pop()] = i
        if stk: left[i] = stk[-1]
        # if stk and nums[stk[-1]] == x:
        #     right[stk.pop()] = i
        #     stk.pop()
        stk.append(i)

    # 计算每一段的个数，初始时是n个n
    cnt = Counter()
    cnt[n] = n
    # 从高到低切割
    idx = sorted(range(n), key = lambda x: - nums[x])
    for i in idx:
        x = nums[i]
        pre = right[i] - left[i] - 1
        l, r = i - left[i] - 1, right[i] - i - 1
        cnt[pre] -= x
        if l: cnt[l] += x
        if r: cnt[r] += x
    
    # print(cnt)
    ans = 0
    # 从最长的段开始计算答案
    # for i in range(n, 1, -1):
    #     k = min(m // i, cnt[i])
    #     ans += k * (i - 1)
    #     m -= k * i
    #     if m == 0: break
    #     if k < cnt[i]:
    #         ans += m - 1
    #         break
    for i, v in sorted(cnt.items(), reverse = True):
        k = min(m // i, v)
        ans += k * (i - 1)
        m -= k * i
        if m == 0: break
        if k < cnt[i]:
            ans += m - 1
            break
    print(ans)

for _ in range(int(input())):
    solve()