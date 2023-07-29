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
DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def solve() -> None:
    n, m = mint()
    g = []
    for _ in range(n):
        g.append(input())
    visited = [[False] * m for _ in range(n)]
    seen = set()
    q = deque()
    visited[1][1] = True
    for d in range(4):
        seen.add((1, 1, d))
        q.append((1, 1, d))
    ans = 1
    while q:
        x, y, d = q.popleft()
        nx, ny = x + DIR[d][0], y + DIR[d][1]
        if nx < 0 or nx >= n or ny < 0 or ny >= m or g[nx][ny] == "#":
            for nd in ((d + 1) % 4, (d - 1) % 4):
                nx, ny = x + DIR[nd][0], y + DIR[nd][1]
                if nx < 0 or nx >= n or ny < 0 or ny >= m or g[nx][ny] == "#" or (nx, ny, nd) in seen: continue
                seen.add((nx, ny, nd))
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    ans += 1
                q.append((nx, ny, nd))
        elif (nx, ny, d) not in seen:
            if not visited[nx][ny]:
                ans += 1
                visited[nx][ny] = True
            seen.add((nx, ny, d))
            q.append((nx, ny, d))
    
    print(ans)

solve()