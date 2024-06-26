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

    '''
    1. 若n是非2的幂的偶数必赢，因为永远可以减去一个奇数因子，给对方一个奇数，如果这个奇数是质数，对方输，否则对方只能减去一个奇数因子，给回来一个不是2的幂的偶数；
    2. 由1可知，若n是奇数，必输；
    3. 若n是2的幂，若减去一个2的倍数但给对方一个非2的幂的偶数，则必输，所以只能减去一个2的倍数给对方仍然是一个2的幂，等价于>>1，所以计算log2(n)，若为偶数则赢（给对方2）；
    '''

    if n & 1:
        print("Bob")
        return
    
    cnt = 0
    while n % 2 == 0:
        cnt += 1
        n >>= 1
    
    print("Bob" if n == 1 and cnt & 1 else "Alice")

for _ in range(int(input())):
    solve()