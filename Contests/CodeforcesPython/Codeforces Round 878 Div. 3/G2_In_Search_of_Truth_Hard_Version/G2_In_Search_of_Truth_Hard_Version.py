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

# region interactive
def printQry(k) -> None:
    s = str(k)
    print(f"+ {s}", flush = True)

def printAns(ans) -> None:
    s = str(ans)
    print(f"! {s}", flush = True)
# endregion interactive

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
    mx = sint()
    for _ in range(100):
        printQry(randint(1, 1e9))
        mx = max(mx, sint())
    
    time = dict()
    for t in range(401):
        printQry(1)
        x = sint()
        if x in time:
            printAns(t)
            return
        time[x] = t
    
    printQry(mx)
    x = sint()
    if x in time:
        printAns(400 + mx - time[x])
        return

    for t in range(1, 401):
        printQry(400)
        x = sint()
        if x in time:
            printAns(mx + (t + 1) * 400 - time[x])
            return

# for _ in range(int(input())):
solve()