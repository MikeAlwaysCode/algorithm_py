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
MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def solve() -> None:
    n, k = mint()

    fa = list(range(n + 1))
    sz = [1] * (n + 1)
    def find(x: int) -> int:
        cur = x
        while x != fa[x]:
            x = fa[x]
        while fa[cur] != x:
            tmp = fa[cur]
            fa[cur] = x
            cur = tmp
        return x
    
    for _ in range(n - 1):
        u, v, c = mint()
        if c == 0:
            fu = find(u)
            fv = find(v)
            if fu != fv:
                sz[fu] += sz[fv]
                fa[fv] = fu
    
    ans = pow(n, k, MOD)
    for i in range(1, n + 1):
        if i == find(i): ans = (ans - pow(sz[i], k, MOD)) % MOD
    print(ans)

# for _ in range(int(input())):
solve()