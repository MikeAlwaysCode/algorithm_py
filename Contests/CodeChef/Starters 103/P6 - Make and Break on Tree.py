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

# MOD = 998244353
# MOD = 10 ** 9 + 7

def solve() -> None:
    n = sint()
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = mint()
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)

    mx = L = -1
    q = deque([(0, 0, -1)])
    while q:
        d, x, p = q.popleft()
        if d > mx:
            mx, L = d, x
        for y in g[x]:
            if y == p: continue
            q.append((d + 1, y, x))
            
    parent = [-1] * n
    ans = mx
    connect_two = False
    q = deque([(L, -1)])
    dis = [0] * n
    while q:
        x, p = q.popleft()
        if dis[x] > ans:
            ans = dis[x]
        for y in g[x]:
            if y == p: continue
            parent[y] = x
            dis[y] = dis[x] + 1
            q.append((y, x))
        if not connect_two and len(g[x]) == 2:
            connect_two = True
    
    if ans == n - 1 or connect_two:
        print(ans)
        return
    

    print(ans + 1)

for _ in range(int(input())):
    solve()