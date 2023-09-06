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
    A = ints()
    s = input()

    ans = 0
    f0 = [0] * 8
    f1 = [0] * 8
    for x, c in zip(A, s):
        if c == 'M':
            f0[1 << x] += 1
        elif c == 'E':
            for v in range(3):
                f1[(1 << x) | (1 << v)] += f0[1 << v]
        else:
            for v in range(1, 8):
                if not f1[v]: continue
                mask = v | (1 << x)
                if mask == 7:
                    ans += 3 * f1[v]
                else:
                    mask ^= 7
                    ans += ((mask & (-mask)).bit_length() - 1) * f1[v]
    '''
    m = [0] * 3
    me = [[0] * 3 for _ in range(3)]
    for x, c in zip(A, s):
        if c == "M":
            m[x] += 1
        elif c == "E":
            for i in range(3):
                j, k = min(x, i), max(x, i)
                me[j][k] += m[i]
        else:
            for i in range(3):
                for j in range(i, 3):
                    for k in range(4):
                        if k != x and k != i and k != j:
                            ans += me[i][j] * k
                            break
    '''
    print(ans)

solve()