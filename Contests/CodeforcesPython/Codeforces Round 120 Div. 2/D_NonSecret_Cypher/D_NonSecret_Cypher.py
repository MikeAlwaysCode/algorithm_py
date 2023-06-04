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
    # nums = input().split()
    nums = ints()

    # 592 ms
    cnt = Counter()
    ans = l = 0
    for x in nums:
        cnt[x] += 1
        while cnt[x] >= k:
            cnt[nums[l]] -= 1
            l += 1
        ans += l

    '''
    # 810 ms
    pos = defaultdict(list)

    ans, p = 0, -1
    for i, x in enumerate(nums):
        pos[x].append(i)
        if len(pos[x]) >= k and pos[x][-k] > p:
            ans += (pos[x][-k] - p) * (n - i)
            p = pos[x][-k]
    '''
    
    '''
    # 904 ms
    d = {v:i for i, v in enumerate(set(nums))}
    pos = [[] for _ in range(len(d))]
    ans, p = 0, -1
    for i, x in enumerate(nums):
        x = d[x]
        pos[x].append(i)
        if len(pos[x]) >= k and pos[x][-k] > p:
            ans += (pos[x][-k] - p) * (n - i)
            p = pos[x][-k]
    '''

    print(ans)


# for _ in range(int(input())):
solve()