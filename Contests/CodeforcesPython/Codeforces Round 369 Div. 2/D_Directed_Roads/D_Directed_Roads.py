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
MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def solve() -> None:
    n = sint()

    edge = ints()
    time = [0] * n
    clock = ans = 1
    for x, t in enumerate(time):
        if t: continue  # 前面访问过的节点
        start_time = clock  # 本次初始时间戳
        while x >= 0:
            if time[x]: # 重复访问的节点
                if time[x] >= start_time: # 时间戳大于等于本次搜索的起始时间戳，代表找到一个环
                    l = clock - time[x]
                    n -= l
                    ans = (ans * (pow(2, l, MOD) - 2)) % MOD
                break
            time[x] = clock
            clock += 1
            x = edge[x] - 1
    ans = ans * pow(2, n, MOD) % MOD
    print(ans)

# for _ in range(int(input())):
solve()