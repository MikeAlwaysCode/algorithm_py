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
    nums.sort()
    ans = set()
    s = 0
    for x in nums:
        cnt = 0
        # 小于当前数的missing才是准确的
        for a in ans:
            if a < x: cnt += 1
        if cnt >= k:
            break
        
        if x > s:
            # x很大时这里直接添加range可能会TLE
            for a in range(s + 1, x):
                ans.add(a)
                if len(ans) == k: break

            # x跟前面的missing会产生新的missing
            for a in sorted(ans):
                if a <= s: ans.add(x + a)
            # ans |= set(range(s + 1, x))
        else:
            ns = set()
            for a in ans:
                # 过滤前面的数产生的missing可能会被当前数填充掉
                if a < x or a - x in ans:
                    ns.add(a)
                if a + x > s or x + a in ans:
                    ns.add(x + a)
            ans = ns

        s += x
    # print(s)
    if len(ans) < k:
        ans |= set(range(s + 1, s + k - len(ans) + 1))
    print(*sorted(ans)[:k])

solve()