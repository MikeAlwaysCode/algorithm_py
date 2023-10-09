import sys
import math
from itertools import *

# from bisect import *
# from collections import *
# from functools import *
# from heapq import *
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
    n, a, b, c = mint()
    nums = ints()
    
    ab, ac, bc, abc = math.lcm(a, b), math.lcm(a, c), math.lcm(b, c), math.lcm(a, b, c)
    
    def zz(x: int, t: int) -> int:
        return (x + t - 1) // t * t - x
    
    ans = math.inf
    op = []
    for x in nums:
        op.append((zz(x, a), zz(x, b), zz(x, c), zz(x, bc), zz(x, ac), zz(x, ab)))
        ans = min(ans, zz(x, abc))

    idx = []
    idx.append(sorted(range(n), key = lambda x: op[x][0]))
    idx.append(sorted(range(n), key = lambda x: op[x][1]))
    idx.append(sorted(range(n), key = lambda x: op[x][2]))
    idx.append(sorted(range(n), key = lambda x: op[x][3]))
    idx.append(sorted(range(n), key = lambda x: op[x][4]))
    idx.append(sorted(range(n), key = lambda x: op[x][5]))

    for p in permutations(range(3)):
        res = 0
        s = set()
        for i in p:
            for j in idx[i]:
                if j not in s:
                    s.add(j)
                    res += op[j][i]
                    break
        if len(s) == 3:
            ans = min(ans, res)
    
    for i in range(3):
        for j in range(min(2, n)):
            for k in idx[i + 3]:
                if k != idx[i][j]:
                    ans = min(ans, op[k][i + 3] + op[idx[i][j]][i])
                    break
    print(ans)

solve()