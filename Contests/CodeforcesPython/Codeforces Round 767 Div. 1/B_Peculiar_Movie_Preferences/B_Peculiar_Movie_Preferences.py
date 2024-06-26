# import math
import sys
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
    # 1，22，33，32，322，332
    n = sint()
    s = set()
    s3 = set()
    ans = False
    for _ in range(n):
        cur = input()
        if not ans:
            if len(cur) == 1 or cur[0] == cur[-1]:
                ans = True
            elif cur[::-1] in s or cur[::-1] in s3:
                # 22, 33, 32
                ans = True
            elif len(cur) == 3:
                if cur[:0:-1] in s:
                    # 23
                    ans = True
                    
                s3.add(cur[:2])

            s.add(cur)
        
    print("YES" if ans else "NO")

for _ in range(int(input())):
    solve()