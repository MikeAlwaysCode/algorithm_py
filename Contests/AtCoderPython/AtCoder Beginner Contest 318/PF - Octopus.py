import math
import sys
from collections import *

# from bisect import *
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
    xp = ints()
    lg = ints()

    d = defaultdict(list)

    for l in lg:
        for i, x in enumerate(xp):
            d[x - l].append((i, 1))
            d[x + l + 1].append((i, -1))
    # print(sorted(d.items()))
    cnt = [0] * n
    k = 0
    ans = 0
    pre = math.inf
    chk = False
    for pos, op in sorted(d.items()):
        for i, v in op:
            if cnt[i] == 0: k += 1
            cnt[i] += v
            if cnt[i] == 0: k -= 1
        if chk and k != n:
            ans += pos - pre
            chk = False
        if not chk and k == n:
            chk = True
            pre = pos
    print(ans)
solve()