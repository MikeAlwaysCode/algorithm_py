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
    n, m = mint()
    s = []
    q = []
    target = set()
    visited = [False] * n
    to = [[] for _ in range(m + 1)]
    for i in range(n):
        a = sint()
        s.append(set(ints()))
        for j in s[-1]:
            if j == 1:
                q.append(i)
                visited[i] = True
            elif j == m:
                target.add(i)
            else:
                to[j].append(i)
    
    step = 0
    while q:
        tmp = []
        for x in q:
            if x in target:
                print(step)
                return
            for y in s[x]:
                for z in to[y]:
                    if visited[z]: continue
                    visited[z] = True
                    tmp.append(z)
        step += 1
        q = tmp

    print(-1)

solve()