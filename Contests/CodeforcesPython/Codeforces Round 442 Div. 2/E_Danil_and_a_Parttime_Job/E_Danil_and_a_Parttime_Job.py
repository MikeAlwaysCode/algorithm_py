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

def dfs(graph, start=0):
    n = len(graph)

    dfn = [-1] * n
    sz = [1] * n
    visited, finished = [False] * n, [False] * n
    time = n - 1

    stack = [start]
    while stack:
        start = stack[-1]

        # push unvisited children into stack
        if not visited[start]:
            visited[start] = True
            for child in graph[start]:
                if not visited[child]:
                    stack.append(child)
        else:
            stack.pop()
            dfn[start] = time
            time -= 1

            # update with finished children
            for child in graph[start]:
                if finished[child]:
                    sz[start] += sz[child]

            finished[start] = True

    return dfn, sz

class SegTree:
    def __init__(self, nums: list) -> None:
        n = len(nums)
        self.n = n
        self.tree = [0] * (4 * n)
        self.lazy = [0] * (4 * n)
        self.build(nums, 1, 1, n)
        
    def build(self, nums: list, o: int, l: int, r: int) -> None:
        if l == r:
            self.tree[o] = nums[l - 1]
            return

        m = (l + r) >> 1
        self.build(nums, o * 2, l, m)
        self.build(nums, o * 2 + 1, m + 1, r)
        self.pushUp(o)

    def xor(self, o: int, l: int, r: int) -> None:
        self.tree[o] = r - l + 1 - self.tree[o] # 异或反转
        self.lazy[o] ^= 1

    def do(self, o: int, l: int, r: int, val: int) -> None:
        self.tree[o] = r - l + 1 - self.tree[o] # 异或反转
        self.lazy[o] ^= 1

    def op(self, a: int, b: int) -> int:
        # + - * / max min
        return a + b
    
    def maintain(self, o: int, l: int, r: int) -> None:
        self.tree[o] = self.op(self.tree[l], self.tree[r])
        self.lazy[o] ^= 1

    def pushUp(self, o: int) -> None:
        self.tree[o] = self.tree[o * 2] + self.tree[o * 2 + 1]

    def pushDown(self, o: int, l: int, r: int) -> None:
        m = (l + r) >> 1
        self.do(o * 2, l, m, self.lazy[o])           # 调用相应的更新操作方法
        self.do(o * 2 + 1, m + 1, r, self.lazy[o])
        self.lazy[o] = 0

    def update(self, o: int, l: int, r: int, L: int, R: int, val: int) -> None:
        if L <= l and r <= R:   # 当前区间已完全包含在更新区间，不需要继续往下更新，存在lazy
            self.xor(o, l, r)
            return

        if self.lazy[o]:    # 当前lazyd存在更新，往下传递
            self.pushDown(o, l, r)

        m = (l + r) >> 1
        if m >= L:  # 左节点在更新区间
            self.update(o * 2, l, m, L, R, val)
        if m < R:   # 右节点在更新区间
            self.update(o * 2 + 1, m + 1, r, L, R, val)

        self.pushUp(o)  # 从左右节点更新当前节点值

    def query(self, o: int, l: int, r: int, L: int, R: int) -> int:
        if R < l or L > r:
            return 0

        if L <= l and r <= R:
            return self.tree[o]

        if self.lazy[o]:    # 当前lazyd存在更新，往下传递
            self.pushDown(o, l, r)

        m = (l + r) >> 1
        res = 0
        if m >= L:  # 左节点在查询区间
            res += self.query(o * 2, l, m, L, R)
        if m < R:   # 右节点在查询区间
            res += self.query(o * 2 + 1, m + 1, r, L, R)

        return res
    
def solve() -> None:
    n = sint()

    p = ints()
    # 建图
    g = [[] for _ in range(n)]
    for i, u in enumerate(p, 1):
        g[u - 1].append(i)

    # DFN序
    dfn, sz = dfs(g)
    # print(dfn)
    # print(sz)

    t = ints()
    nums = [0] * n
    for i, v in enumerate(t):
        nums[dfn[i]] = v
    # print(nums)
    st = SegTree(nums)

    for _ in range(sint()):
        qry = input().split()
        u = int(qry[1]) - 1
        if qry[0] == "get":
            print(st.query(1, 1, n, dfn[u] + 1, dfn[u] + sz[u]))
        else:
            st.update(1, 1, n, dfn[u] + 1, dfn[u] + sz[u], 1)

# for _ in range(int(input())):
solve()