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

class BIT:
    def __init__(self, n: int):
        self.nums = [0] * (n + 1)
        self.n = n
        self.BITree = [0] * (self.n + 1)
        
    def lowbit(self, x: int) -> int:
        return x & -x
    
    def query(self, x: int) -> int:
        ans = 0
        while x:
            ans += self.BITree[x]
            x -= self.lowbit(x)
        return ans

    def add(self, x: int, val: int):
        while x <= self.n:
            self.BITree[x] += val
            x += self.lowbit(x)

    def update(self, x: int, val: int) -> None:
        self.add(x + 1, val - self.nums[x])
        self.nums[x] = val

def solve() -> None:
    n = sint()
    a = []
    s = set()
    for _ in range(n):
        a.append(ints())
        a[-1].sort()
        s = s.union(set(a[-1]))
    a.sort()
    
    disc = {v:i for i, v in enumerate(sorted(s))}
    m = len(s)
    
    def check(l: int, r: int) -> bool:
        if l == r: return False
        mid = (l + r) >> 1
        if check(l, mid) or check(mid + 1, r): return True
        a[l:mid + 1] = sorted(a[l: mid + 1], key = lambda x: x[1])
        a[mid + 1:r + 1] = sorted(a[mid + 1: r + 1], key = lambda x: x[1])
        bit = BIT(m)
        j = l
        for i in range(mid + 1, r + 1):
            while j <= mid and a[j][1] <= a[i][1]:
                bit.update(disc[a[j][2]], 1)
                j += 1
            if bit.query(disc[a[i][2]]) > 0: return True
        return False
    
    print("Yes" if check(0, n - 1) else "No")

solve()