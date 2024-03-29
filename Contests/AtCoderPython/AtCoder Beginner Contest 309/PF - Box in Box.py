import math
import sys

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

class BIT:
    def __init__(self, n: int):
        self.n = n
        self.BITree = [math.inf] * (self.n + 1)
        
    def lowbit(self, x: int) -> int:
        return x & -x
    
    def query(self, x: int) -> int:
        ans = math.inf
        x += 1
        while x:
            ans = min(ans, self.BITree[x])
            x -= self.lowbit(x)
        return ans

    def update(self, x: int, val: int) -> None:
        x += 1
        while x <= self.n:
            self.BITree[x] = min(self.BITree[x], val)
            x += self.lowbit(x)

def solve() -> None:
    n = sint()
    a = []
    s = set()
    for _ in range(n):
        a.append(ints())
        a[-1].sort()
        s.add(a[-1][1])

    a.sort()
    
    disc = {v:i for i, v in enumerate(sorted(s))}
    m = len(s)

    bit = BIT(m)
    i = 0
    while i < n:
        j = i
        while j < n and a[j][0] == a[i][0]:
            if bit.query(disc[a[j][1]] - 1) < a[j][2]:
                print("Yes")
                return
            j += 1

        while i < j:
            bit.update(disc[a[i][1]], a[i][2])
            i += 1
    
    print("No")

solve()