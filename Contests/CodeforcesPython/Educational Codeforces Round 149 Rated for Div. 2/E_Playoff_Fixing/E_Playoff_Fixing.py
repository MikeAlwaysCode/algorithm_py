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

MOD = 998244353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def solve() -> None:
    k = sint()
    arr = ints()

    if k == 0:
        print(1)
        return
    
    # 阶乘
    m = 1 << (k - 1)
    fact = [1] * (m + 1)
    for i in range(1, m + 1):
        fact[i] = fact[i-1] * i % MOD

    # for i, a in enumerate(arr):
    #     if a != -1: arr[i] -= 1

    ans = step = 1
    while k:
        p, pow2 = 0, 1

        # 这一轮需要淘汰的编号范围
        L, R = (1 << (k - 1)) + 1, 1 << k
        for i in range(1 << (k - 1)):
            # 这一轮battle的两个位置
            l, r = i * step * 2, i * step * 2 + step
            x, y = arr[l], arr[r]
            if x == y == -1:
                pow2 = pow2 * 2 % MOD
                p += 1
            else:
                if x > y:
                    x, y = y, x
                if x == -1:
                    if L <= y <= R:
                        # y 被淘汰，x只能放晋级数
                        arr[l] = -1
                    else:
                        # y 需要晋级，x可以随便填一个淘汰数
                        arr[l] = y
                        p += 1
                elif x < L <= y <= R:
                    arr[l] = x
                else:
                    print(0)
                    return
        
        ans = ans * pow2 * fact[p] % MOD

        k -= 1
        step <<= 1

    print(ans)

# for _ in range(int(input())):
solve()