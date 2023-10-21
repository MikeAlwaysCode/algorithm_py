import sys

# import math
# import os
# import random
# from bisect import bisect, bisect_left
# from collections import *
# from functools import reduce
# from heapq import heapify, heappop, heappush
# from itertools import *
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

# region dfsconvert
from types import GeneratorType
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

# MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR4 = ((-1, 0), (0, 1), (1, 0), (0, -1)) #URDL
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

def solve() -> None:
    n = sint()
    nums = ints()
    
    left = [-1] * n
    right = [-1] * n
    
    stack = []
    for i in range(n):
        num = nums[i]
        idx = -1
        while len(stack) and nums[stack[-1]] >= num:
            new_idx = stack.pop()
            right[new_idx] = idx
            idx = new_idx
        if idx != -1: left[i] = idx
        stack.append(i)
    
    idx = -1
    root = stack[0]
    while len(stack):
        new_idx = stack.pop()
        right[new_idx] = idx
        idx = new_idx
    
    @bootstrap
    def dfs(root, curr, tot_left, tot_right):
        ans = 0
        if left[root] != -1:
            l = left[root]
            yield dfs(l, nums[root], tot_left, root - 1)
            ans += mem[l]
        if right[root] != -1:
            r = right[root]
            yield dfs(r, nums[root], root + 1, tot_right)
            ans += mem[r]
        mem[root] = min(ans + nums[root] - curr, tot_right - tot_left + 1)
        yield
    
    mem = [None] * n
    dfs(root, 0, 0, n - 1)
    print(mem[root])

solve()