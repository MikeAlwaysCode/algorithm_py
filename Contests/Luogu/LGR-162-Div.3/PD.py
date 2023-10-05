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

class RangeLink:
    def __init__(self, n: int) -> None:
        self.vals = [1] * n
        self.s = 0
        self.nxt = list(range(1, n + 1))
    
    def modify(self, l: int, r: int) -> None:
        x = l
        while x <= r:
            if self.vals[x]: self.s += 1
            self.vals[x] = 0
            self.nxt[x], x = self.nxt[r], self.nxt[x]
    
    def query(self, l: int, r: int) -> int:
        res = 0
        x = l
        while x <= r:
            res += self.vals[x]
            x = self.nxt[x]
        return res

def solve() -> None:
    n, m, k, q = mint()
    ans = [0] * k
    qry = [[] for _ in range(2)]
    for _ in range(q):
        op, l, r, c, t = mint()
        qry[t].append((op, l, r, c - 1))
        
    row, col = RangeLink(n), RangeLink(m)

    for op, l, r, c in qry[1][::-1]:
        if op == 1: # row
            rc, cc = row.query(l - 1, r - 1), col.s
            ans[c] += rc * (m - cc)
            row.modify(l - 1, r - 1)
        else:       # col
            rc, cc = row.s, col.query(l - 1, r - 1)
            ans[c] += (n - rc) * cc
            col.modify(l - 1, r - 1)

    for op, l, r, c in qry[0]:
        if op == 1: # row
            rc, cc = row.query(l - 1, r - 1), col.s
            ans[c] += rc * (m - cc)
            row.modify(l - 1, r - 1)
        else:       # col
            rc, cc = row.s, col.query(l - 1, r - 1)
            ans[c] += (n - rc) * cc
            col.modify(l - 1, r - 1)
    
    print(*ans)

solve()