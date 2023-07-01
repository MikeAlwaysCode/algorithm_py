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
    h, w = mint()
    maze = []
    for _ in range(h):
        maze.append(input())
    
    if maze[0][0] != "s":
        print("No")
        return
    
    seen = [[False] * w for _ in range(h)]
    seen[0][0] = True
    t = "snuke"
    q = deque([(0, 0, 0)])
    while q:
        x, y, d = q.popleft()
        for nx, ny in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
            if nx < 0 or nx >= h or ny < 0 or ny >= w or seen[nx][ny]: continue
            if maze[nx][ny] != t[(d + 1) % 5]: continue
            if nx == h - 1 and ny == w - 1:
                print("Yes")
                return
            seen[nx][ny] = True
            q.append((nx, ny, (d + 1) % 5))
    print("No")

solve()