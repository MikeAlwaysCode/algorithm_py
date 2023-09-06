import sys
# from collections import *
# from heapq import *
from types import GeneratorType

# import math
# from bisect import *
# from functools import *
# from itertools import *
# from random import *
# from string import *

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

# region dfsconvert
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc
# endregion dfsconvert

# MOD = 998244353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def solve() -> None:
    n, m = mint()
    g = [[] for _ in range(n + 1)]
    # incnt, outcnt = [0] * (n + 1), [0] * (n + 1)
    incnt = [0] * (n + 1)
    for _ in range(m):
        u, v = mint()
        g[u].append(v)
        # outcnt[u] += 1
        incnt[v] += 1
    
    start = -1
    end = -1
    # for i, (ic, oc) in enumerate(zip(incnt, outcnt)):
    for i, ic in enumerate(incnt):
        if len(g[i]) == ic + 1:
            if start == -1:
                start = i
            else:
                print("No")
                return
        elif ic == len(g[i]) + 1:
            if end == -1:
                end = i
            else:
                print("No")
                return
        elif ic != len(g[i]):
            print("No")
            return
    
    if (start == -1) != (end == -1):
        print("No")
        return

    if start == -1:
        start = 1

    for k in range(1, n + 1):
        # heapify(g[k])
        g[k].sort(reverse = True)

    ans = []

    @bootstrap
    def dfs(x: int):
        while g[x]:
            # y = heappop(g[x])
            y = g[x].pop()
            yield dfs(y)
        ans.append(x)
        yield
    
    dfs(start)
    print(*ans[::-1])

solve()