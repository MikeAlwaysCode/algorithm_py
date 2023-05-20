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
    A = ints()
    B = sorted(A)
    ans = 0
    cnt = Counter()
    for i in range(n):
        if A[i] == B[i]: continue
        if cnt[(B[i], A[i])]:
            cnt[(B[i], A[i])] -= 1
            ans += 1
        else:
            cnt[(A[i], B[i])] += 1
    
    for k, v in cnt.items():
        if v == 0: continue
        while v:
            fr, to = k
            while cnt[(to, fr)] == 0:
                for nxt in range(1, 5):
                    if cnt[(to, nxt)]:
                        cnt[(to, nxt)] -= 1
                        to = nxt
                        ans += 1
                        break
            cnt[k] -= 1
            cnt[(to, fr)] -= 1
            ans += 1
            v -= 1
    print(ans)

solve()