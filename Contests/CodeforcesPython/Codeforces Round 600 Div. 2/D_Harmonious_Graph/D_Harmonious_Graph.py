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

    fa = list(range(n))
    mx = list(range(n))

    def find(x: int):
        cur = x
        while x != fa[x]:
            x = fa[x]
        while fa[cur] != x:
            # fa[cur], cur = x, fa[cur]
            tmp = fa[cur]
            fa[cur] = x
            cur = tmp
        return x
    def union(x: int, y: int):
        x, y = find(x), find(y)
        if x == y: return
        # 往较小的点合并
        if x > y: x, y = y, x
        fa[y] = x
        # 保存整个连通块中的最大点
        mx[x] = max(mx[x], mx[y])

    for _ in range(m):
        u, v = mint()
        u -= 1
        v -= 1
        union(u, v)
    
    ans = i = 0
    while i < n:
        j = i + 1
        while j < mx[i]:
            if find(j) != i:
                # 发现一个范围内的不连通点，则加一条边，如果有新的更大点，会更新至mx[i]
                union(i, j)
                ans += 1
            j += 1
        i = mx[i] + 1
    print(ans)

# for _ in range(int(input())):
solve()