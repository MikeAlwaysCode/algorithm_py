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

def solve() -> None:
    n = sint()
    arr = ints()
    odd = sum(a & 1 for a in arr)
    even = n - odd
    # 1. 记奇数个数为odd， 偶数个数为even；
    # 2. 记k为(odd + 1) // 2，若k为偶数，则Alice必定可以合成k对奇数，Alice赢；
    # 3. 否则，若odd为偶数，每次Alice选择一个奇数时，Bob也跟着选择一个奇数，Bob赢；
    # 4. 若even为偶数，即使odd为奇数，假设剩下一个奇数时，Bob的策略可以使得最后这个奇数一定是Alice选择，Bob赢；
    print("Alice" if not (odd + 1) >> 1 & 1 or (odd & 1 and even & 1) else "Bob")

for _ in range(int(input())):
    solve()