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
    r = sint()
    rg = set()
    for _ in range(r):
        rg.add((tuple(mint())))
        
    '''
    # 1528 ms
    dp = [[[0] * (m + 1) for _ in range(n + 1)] for _ in range(r + 10)]
    dp[0][0][0] = 1
    for i in range(r + 10):
        for x in range(n + 1):
            for y in range(m + 1):
                if not dp[i][x][y]: continue
                t = i + x + y
                if (t, 1, x) in rg or (t, 2, y) in rg:
                    dp[i][x][y] = 0
                    continue
                if i + 1 < r + 10:
                    dp[i + 1][x][y] = 1
                if x < n:
                    dp[i][x + 1][y] = 1
                if y < m:
                    dp[i][x][y + 1] = 1
        # 1325 ms
        if dp[i][n][m]:
            print(i + n + m)
            return

    # ans = math.inf
    # for i in range(r + 10):
    #     if dp[i][n][m]: ans = min(ans, i + n + m)
    # print(-1 if ans == math.inf else ans)
    '''
    
    # MLE
    q = deque([(0, 0, 0)])
    visited = set()
    while q:
        t, x, y = q.popleft()
        if (t, 1, x) in rg or (t, 2, y) in rg: continue

        if x == n and y == m:
            print(t)
            return
        
        if t > x + y + r: continue
        
        if (t + 1, x, y) not in visited:
            visited.add((t + 1, x, y))
            q.append((t + 1, x, y))

        if x + 1 <= n and (t + 1, x + 1, y) not in visited:
            visited.add((t + 1, x + 1, y))
            q.append((t + 1, x + 1, y))

        if y + 1 <= m and (t + 1, x, y + 1) not in visited:
            visited.add((t + 1, x, y + 1))
            q.append((t + 1, x, y + 1))
    
    print(-1)

for _ in range(int(input())):
    solve()