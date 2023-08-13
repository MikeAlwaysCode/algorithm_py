import sys

# import math
# from bisect import *
# from collections import *
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
    n, m = mint()
    edges = [[[] for _ in range(2)] for _ in range(n)]
    col_edge = [[] for _ in range(2)]
    for i in range(1, m + 1):
        e = input().split()
        u = int(e[0]) - 1
        v = int(e[1]) - 1
        c = 0 if e[2] == "R" else 1
        edges[u][c].append((v, i))
        edges[v][c].append((u, i))
        col_edge[c].append((u, v, i))
    s = [0 if c == "R" else 1 for c in input()]
    
    fa = list(range(n))
    sz = [1] * n
    set_count = n
    def find(x: int):
        cur = x
        while x != fa[x]:
            x = fa[x]
        while fa[cur] != x:
            fa[cur], cur = x, fa[cur]
        return x

    def union(fr: int, to: int):
        nonlocal set_count
        set_count -= 1
        sz[to] += sz[fr]
        sz[fr] = 0
        fa[fr] = to

    ans = []
    for c in range(2):
        for u, v, i in col_edge[c]:
            if s[u] == s[v] == c:
                fu, fv = find(u), find(v)
                if fu != fv:
                    ans.append(i)
                    union(fu, fv)
    
    # for u in range(n):
    #     fu = find(u)
    #     c = s[fu]
    #     if sz[fu] != 1:
    #         continue
    #     else:
    #         for v, i in edges[fu][c]:
    #             fv = find(v)
    #             if sz[fv] > 1:
    #                 ans.append(i)
    #                 union(fu, fv)
    #                 break
    
    if set_count == 1:
        print("Yes")
        print(*ans)
        return
        
    seen = set()
    q = []
    for u in range(n):
        fu = find(u)
        if sz[fu] == 1: continue
        for c in range(2):
            for v, i in edges[u][c]:
                fv = find(v)
                if fu == fv: continue

                if sz[fv] > 1:
                    ans.append(i)
                    union(fu, fv)
                elif sz[fv] == 1 and fv not in seen and c == s[fv]:
                    seen.add(fv)
                    q.append((fu, fv, i))

                if set_count == 1: break
            if set_count == 1: break
    
    while q:
        tmp = []
        for u, v, i in q:
            fu, fv = find(u), find(v)
            if fu == fv or sz[fv] != 1: continue
            ans.append(i)
            union(fu, fv)
            for c in range(2):
                for w, j in edges[v][c]:
                    fw = find(w)
                    if sz[fw] != 1 or fw in seen or c != s[fw]: continue
                    seen.add(fw)
                    tmp.append((fv, fw, j))
        q = tmp

    for u in range(n):
        fu = find(u)
        if sz[fu] == 1: continue
        for c in range(2):
            for v, i in edges[u][c]:
                fv = find(v)
                if fu == fv: continue

                if sz[fv] > 1:
                    ans.append(i)
                    union(fu, fv)

                if set_count == 1: break
            if set_count == 1: break

    if set_count > 1:
        print("No")
    else:
        print("Yes")
        print(*ans)

solve()