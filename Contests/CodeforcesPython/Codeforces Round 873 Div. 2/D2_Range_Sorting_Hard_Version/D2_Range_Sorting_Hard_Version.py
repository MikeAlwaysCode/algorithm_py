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
    arr = ints()

    # 0 * 1 / 2 + 1 * 2 / 2 + ... + (n - 1) * n / 2 = (n - 1) * n * (n + 1) / 6
    ans = (n - 1) * n * (n + 1) // 6

    # left: 左边第一个小于a[i]的位置；right: 右边第一个小于a[i]的位置; ai: 被k[i]弹出的ai
    left, right, stk, ai = [-1] * n, [n] * n, [], []

    for i in range(n - 1, -1, -1):
        # 前面被left[i]弹出的a[i]，若小于当前元素，此时i即为a[i]的左边第一个小于a[i]的位置左边的第一个大于a[i]的位置
        while ai and arr[ai[-1]] < arr[i]:
            k = ai.pop()
            ans -= (left[k] - i) * (right[k] - k)

        # 单调递增栈，求出右边第一个小于a[i]的位置right[i]，左边第一个小于a[i]的位置left[i]
        while stk and arr[stk[-1]] > arr[i]:
            ai.append(stk.pop())
            left[ai[-1]] = i
        if stk: right[i] = stk[-1]
        stk.append(i)
    
    # 前面被left[i]弹出的a[i]，前面没有大于其的元素，则(l - (-1)) * (r - i)
    while ai:
        k = ai.pop()
        ans -= (left[k] + 1) * (right[k] - k)

    print(ans)

for _ in range(int(input())):
    solve()