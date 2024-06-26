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

    ans = 0
    p = pt = -1
    left = [0] * 2
    border = []
    cnt = [[] for _ in range(2)]

    for i, a in enumerate(arr):
        left[(i + 1) & 1] += 1

        if a == 0: continue

        left[a & 1] -= 1
        
        if p == -1:
            if i: border.append((i, a & 1))
        elif i - p - 1:
            if a & 1 == pt:
                cnt[pt].append(i - p - 1)
            else:
                # 两边奇偶性不同，是否填充无意义，+1
                ans += 1
        else:
            # 相邻且奇偶不同，必定+1
            ans += int(a & 1 != pt)

        p, pt = i, a & 1
        
    if p != n - 1: border.append((n - 1 - p, pt & 1))

    # 优先填充两边奇偶性相同的段
    for i in range(2):
        cnt[i].sort()
        for x in cnt[i]:
            if left[i] >= x:
                left[i] -= x
            else:
                ans += 2

    # 填充两边的段
    border.sort()
    for x, t in border:
        if left[t] >= x:
            left[t] -= x
        else:
            ans += 1
    
    print(ans)
        

# for _ in range(int(input())):
solve()