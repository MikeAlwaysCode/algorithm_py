import math
import sys
from bisect import *
from collections import *
from functools import *
from heapq import *
from itertools import *
from random import *
from string import *

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# print = lambda d: sys.stdout.write(str(d) + " ")
# endregion fastio

# MOD = 998244353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def solve() -> None:
    n, w, h = mint()

    envelope = []
    for i in range(1, n + 1):
        wi, hi = mint()
        if wi > w and hi > h:
            envelope.append((wi, -hi, i))
    
    if not envelope:
        print(0)
        return
    
    envelope.sort(reverse = True)
    
    p = [-1] * (n + 1)
    d = []
    for w, h, i in envelope:
        if not d:
            d.append((h, i))
        elif h > d[-1][0]:
            p[i] = d[-1][1]
            d.append((h, i))
        else:
            j = bisect(d, (h, 0))
            if j: p[i] = d[j - 1][1]
            d[j] = (h, i)
            
    print(len(d))
    ans = []
    j = d[-1][1]
    while j >= 0:
        ans.append(j)
        j = p[j]
    print(*ans)

# for _ in range(int(input())):
solve()

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
# from types import GeneratorType
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