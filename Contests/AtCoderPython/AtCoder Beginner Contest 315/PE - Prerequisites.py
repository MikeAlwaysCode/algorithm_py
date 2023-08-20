import sys
from collections import *

# import math
# from bisect import *
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
    n = sint()
    g = [[] for _ in range(n + 1)]
    to = [[] for _ in range(n + 1)]
    deg = [0] * (n + 1)
    for i in range(1, n + 1):
        g[i] = ints()[1:]
        deg[i] = len(g[i])
        for j in g[i]:
            to[j].append(i)

    seen = [False] * (n + 1)
    q = deque([1])
    while q:
        x = q.popleft()
        for y in g[x]:
            if seen[y]: continue
            seen[y] = True
            q.append(y)

    ans = []
    q = deque([i for i in range(1, n + 1) if seen[i] and deg[i] == 0])
    while q:
        x = q.popleft()
        ans.append(x)
        for y in to[x]:
            deg[y] -= 1
            if seen[y] and deg[y] == 0:
                q.append(y)

    print(*ans)

solve()