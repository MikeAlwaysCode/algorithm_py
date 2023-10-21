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
    n = sint()
    nums = [0] + ints()

    # 数字对应的下标
    idx = [0] * (n + 1)
    for i, v in enumerate(nums):
        idx[v] = i
    
    fa = list(range(n + 1))
    mx = list(range(n + 1))
    def find(x: int):
        cur = x
        while x != fa[x]:
            x = fa[x]
        while fa[cur] != x:
            fa[cur], cur = x, fa[cur]
        return x

    def union(x: int, y: int):
        x, y = find(x), find(y)
        fa[x] = y
        mx[y] = max(mx[x], mx[y])

    seen = [False] * (n + 1)
    for i in range(1, n + 1):
        if seen[i]: continue
        x = i
        while not seen[x]:
            seen[x] = True
            union(x, i)
            x = nums[x]
    # print(fa)
    # print(mx)
    curr = 2
    for i in range(1, n):
        while curr <= n and find(i) == find(curr) and curr <= nums[i]:
            # 与当前不连通的最小数字
            curr += 1
        if curr > n: break
        if i == mx[find(i)] or curr < nums[i]:
            union(curr, i)
            nums[i], nums[idx[curr]] = curr, nums[i]
            idx[curr], idx[nums[i]] = i, idx[curr]
            curr += 1
    
    print(*nums[1:])

for _ in range(sint()):
    solve()