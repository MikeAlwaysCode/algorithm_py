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

def solve() -> None:
    n = sint()
    A0, A1 = ints(), []
    B0, B1 = ints(), []
    ans = 0

    for bit in range(30):
        mask = (1 << bit) - 1

        # A1 = [x for x in A if x >> bit & 1]
        # A0 = [x for x in A if not x >> bit & 1]
        # B1 = [x for x in B if x >> bit & 1]
        # B0 = [x for x in B if not x >> bit & 1]
        TA = A0 + A1
        TB = B0 + B1
        A1 = [x for x in TA if x >> bit & 1]
        A0 = [x for x in TA if not x >> bit & 1]
        B1 = [x for x in TB if x >> bit & 1]
        B0 = [x for x in TB if not x >> bit & 1]

        cnt = 0
        l0, l1 = len(B0) - 1, len(B1) - 1
        for x in A0:
            x &= mask
            while l0 >= 0 and x + (B0[l0] & mask) > mask:
                l0 -= 1
            while l1 >= 0 and x + (B1[l1] & mask) > mask:
                l1 -= 1
            cnt += len(B0) - l0 + l1

        l0, l1 = len(B1) - 1, len(B0) - 1
        for x in A1:
            x &= mask
            while l0 >= 0 and x + (B1[l0] & mask) > mask:
                l0 -= 1
            while l1 >= 0 and x + (B0[l1] & mask) > mask:
                l1 -= 1
            cnt += len(B1) - l0 + l1
        
        ans |= (cnt & 1) << bit

    '''
    for bit in range(29):
        mask = (1 << (bit + 1)) - 1

        A.sort(key = lambda x: x & mask)
        B.sort(key = lambda x: x & mask)
        cnt = 0
        i = j = k = n - 1
        l1, l2, l3 = 1 << bit, (1 << (bit + 1)) - 1, 3 << bit
        for a in A:
            while i >= 0 and (a & mask) + (B[i] & mask) >= l1:
                i -= 1
            while j >= 0 and (a & mask) + (B[j] & mask) > l2:
                j -= 1
            while k >= 0 and (a & mask) + (B[k] & mask) >= l3:
                k -= 1
            cnt ^= i ^ j ^ k
        ans |= (cnt & 1) << bit
    '''
    print(ans)

solve()