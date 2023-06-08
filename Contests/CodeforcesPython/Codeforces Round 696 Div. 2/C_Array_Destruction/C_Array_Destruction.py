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
    nums.sort()
    cnt = Counter(nums)
    for i in range(n * 2 - 1):
        # 确定第一个大数必定是最大数，逐一尝试所有其他较小数
        d = cnt.copy()
        j = n * 2 - 1
        x = nums[i] + nums[j]
        ans = []
        for _ in range(n):
            while j > 0 and d[nums[j]] == 0:
                j -= 1
            d[nums[j]] -= 1
            d[x - nums[j]] -= 1
            if d[nums[j]] < 0 or d[x - nums[j]] < 0:
                break
            ans.append((nums[j], x - nums[j]))
            x = max(nums[j], x - nums[j])
        if len(ans) == n:
            print("YES")
            print(sum(ans[0]))
            for p in ans:
                print(*p)
            return
            
    print("NO")

for _ in range(int(input())):
    solve()