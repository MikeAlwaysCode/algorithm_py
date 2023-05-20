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
    
    ans = [0] * n

    # 堆 265ms
    pos = [0] * (n + 1)
    for i, a in enumerate(arr):
        if pos[a]:
            print(-1)
            return

        ans[i * 2 + 1] = a
        pos[a] = i * 2 + 1
    
    h = []
    for x in range(n, 0, -1):
        if pos[x]:
            heappush(h, - pos[x])
        elif h:
            ans[- heappop(h) - 1] = x
        else:
            print(-1)
            return

    '''
    # 并查集 623ms
    s = set(arr)
    if len(s) < n // 2:
        print(-1)
        return
    
    fa = list(range(n + 1))
    def find(x: int) -> int:
        cur = x
        while x != fa[x]:
            x = fa[x]
        while fa[cur] != x:
            tmp = fa[cur]
            fa[cur] = x
            cur = tmp
        return x

    for i in range(n // 2 - 1, -1, -1):
        k = find(arr[i] - 1)
        while k in s:
            k = find(k - 1)
        if k <= 0:
            print(-1)
            return
        fa[k] = fa[arr[i] - 1] = fa[arr[i]] = k - 1

        ans[i * 2], ans[i * 2 + 1] = k, arr[i]
    '''

    print(*ans)

for _ in range(int(input())):
    solve()