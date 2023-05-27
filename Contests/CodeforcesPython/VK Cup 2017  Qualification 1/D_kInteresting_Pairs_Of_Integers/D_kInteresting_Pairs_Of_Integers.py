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

def bit_count(x):
    x = (x & 0x55555555) + ((x >> 1) & 0x55555555)
    x = (x & 0x33333333) + ((x >> 2) & 0x33333333)
    x = (x & 0x0f0f0f0f) + ((x >> 4) & 0x0f0f0f0f)
    x = (x & 0x00ff00ff) + ((x >> 8) & 0x00ff00ff)
    x = (x & 0x0000ffff) + ((x >> 16) & 0x0000ffff)
    return x

def solve() -> None:
    n, k = mint()
    arr = ints()

    # 数据范围2^14，位数是低7位的数归类
    bits = [[] for _ in range(8)]
    for i in range(1 << 7):
        bits[bit_count(i)].append(i)
    
    ans = 0
    
    '''
    # 342 ms
    # cnt = Counter()
    m = [[0] * (1 << 14) for _ in range(15)]
    for x in arr:
        for i in range(min(8, k + 1)):
            for num in bits[i]:
                # 高位k - i个 * 低位i个
                # ans += cnt[(k - i, x ^ num)]
                ans += m[k - i][x ^ num]
        
        for i in range(min(8, k + 1)):
            for num in bits[i]:
                # cnt[(i, x ^ (num << 7))] += 1
                m[i][x ^ (num << 7)] += 1

    '''
    # 155 ms
    m = [[0] * (1 << 14) for _ in range(15)]
    cnt = Counter(arr)
    for x, v in cnt.items():
        if k == 0: # k为0 直接C(n, 2)
            ans += v * (v - 1) // 2
        else:
            for i in range(min(8, k + 1)):
                for num in bits[i]:
                    # 高位k - i个 * 低位i个
                    ans += m[k - i][x ^ num] * v
            
            for i in range(min(8, k + 1)):
                for num in bits[i]:
                    m[i][x ^ (num << 7)] += v

    print(ans)

# for _ in range(int(input())):
solve()