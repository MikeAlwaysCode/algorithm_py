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
MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def solve() -> None:
    n = sint()
    nums = ints()
    xor, cnt0 = 0, 1
    f0 = [1] * (1 << 20)
    f1 = [0] * (1 << 20)
    c0 = [0] * (1 << 20)
    for x in nums:
        xor ^= x
        if xor == 0:
            cnt0 += 1
        else:
            # 跟上一个异常值是xor的位置之间异或值是0的位置，都能得到异或值是0的分割
            f0[xor] = (f0[xor] + f1[xor] * (cnt0 - c0[xor])) % MOD
            # 前面所有异或值为0的方案
            f1[xor] = (f0[xor] + f1[xor]) % MOD
            c0[xor] = cnt0

    if xor:
        print(f0[xor])
    else:
        ans = (pow(2, cnt0 - 2, MOD) + sum(f1)) % MOD
        print(ans)

solve()