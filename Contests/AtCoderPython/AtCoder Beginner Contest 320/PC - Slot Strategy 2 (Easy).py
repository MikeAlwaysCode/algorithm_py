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

def solve() -> None:
    m = sint()
    t = [[[] for _ in range(3)] for _ in range(10)]
    for i in range(3):
        s = input()
        for j in range(m):
            d = int(s[j])
            t[d][i].append(j)
    ans = math.inf
    for td in t:
        if not td[0] or not td[1] or not td[2]: continue
        for i in td[0]:
            for j in td[1]:
                res_ij = i + m if i == j else max(i, j)
                for k in td[2]:
                    if k == i == j:
                        res = i + m * 2
                    elif k == i:
                        res = max(i + m, j)
                    elif k == j:
                        res = max(j + m, i)
                    else:
                        res = max(res_ij, k)
                    ans = min(ans, res)
        
    print(-1 if ans == math.inf else ans)

solve()