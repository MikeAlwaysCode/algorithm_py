import math
import sys
from collections import *
from heapq import heapify, heappop, heappush

# import itertools
# import os
# import random
# from bisect import bisect, bisect_left
# from functools import reduce
# from io import BytesIO, IOBase
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

# # region dfsconvert
# from types import GeneratorType
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
    nums = ints()
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = mint()
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)

    def zz(x: int, bit: int) -> int:
        return bit * n + x

    m = n.bit_length()
    # 节点深度
    depth = [0] * n
    # 倍增父节点
    # pa = [[-1] * m for _ in range(n)]
    pa = [-1] * (n * 31)
    # 最近的位上是1的祖先
    # up = [[-1] * 31 for _ in range(n)]
    up = [-1] * (n * 31)
    # 节点位上1的计数
    # cnt = [[0] * 31 for _ in range(n)]
    cnt = [0] * (n * 31)
    
    q = deque([(0, -1)])
    while q:
        x, p = q.popleft()

        # 预处理当前节点每位上面哪一层祖先是1
        for bit in range(31):
            if p != -1:
                up[zz(x, bit)] = up[zz(p, bit)]
                cnt[zz(x, bit)] = cnt[zz(p, bit)]
            if (nums[x] >> bit) & 1:
                up[zz(x, bit)] = depth[x]
                cnt[zz(x, bit)] += 1
                
        for y in g[x]:
            if y == p:
                continue
            depth[y] = depth[x] + 1
            pa[zz(y, 0)] = x
            q.append((y, x))

    # 倍增
    for i in range(m - 1):
        for x in range(n):
            if (p := pa[zz(x, i)]) != -1:
                pa[zz(x, i + 1)] = pa[zz(p, i)]

    # 求第k个祖先
    def get_kth_ancestor(node: int, k: int) -> int:
        for i in range(k.bit_length()):
            if (k >> i) & 1:  # k 二进制从低到高第 i 位是 1
                node = pa[zz(node, i)]
        return node

    # 求最近公共祖先
    def get_lca(x: int, y: int) -> int:
        if depth[x] > depth[y]:
            x, y = y, x
        # 使 y 和 x 在同一深度
        y = get_kth_ancestor(y, depth[y] - depth[x])
        if y == x:
            return x
        for i in range(m - 1, -1, -1):
            px, py = pa[zz(x, i)], pa[zz(y, i)]
            if px != py:
                x, y = px, py  # 同时上跳 2**i 步
        return pa[zz(x, 0)]
    
    # 求离公共祖先最近1的计数相同的节点
    def get_top(x: int, p: int, bit: int) -> int:
        for i in range(m - 1, -1, -1):
            if (px := pa[zz(x, i)]) != -1:
                if cnt[zz(px, bit)] > cnt[zz(p, bit)]:
                    x = px
        return x

    ans = []
    for _ in range(sint()):
        x, y = mint()
        x -= 1
        y -= 1

        rng = []
        lca = get_lca(x, y)
        for bit in range(31):
            l, r = math.inf, -math.inf
            if up[zz(x, bit)] >= depth[lca]:
                l = depth[lca] - up[zz(x, bit)]
            elif cnt[zz(y, bit)] > cnt[zz(lca, bit)]:
                l = depth[get_top(y, lca, bit)] - depth[lca]
            
            if up[zz(y, bit)] >= depth[lca]:
                r = up[zz(y, bit)] - depth[lca]
            elif cnt[zz(x, bit)] > cnt[zz(lca, bit)]:
                r = depth[lca] - depth[get_top(x, lca, bit)]
            
            if r >= l:
                rng.append((l, r))
        
        res = len(rng)
        rng.sort()
        h = []
        for l, r in rng:
            while h and h[0] < l:
                heappop(h)
            heappush(h, r)
            res = max(res, len(rng) + len(h))

        ans.append(res)

    print(*ans)


for _ in range(int(input())):
    solve()
