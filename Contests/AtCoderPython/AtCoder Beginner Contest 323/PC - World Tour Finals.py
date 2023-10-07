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
    n, m = mint()
    vals = ints()
    score = [0] * n
    unsol = [set() for _ in range(n)]
    mx, cnt = -1, 0
    for i in range(n):
        s = input()
        cur = i + 1
        for j in range(m):
            if s[j] == 'o':
                cur += vals[j]
            else:
                unsol[i].add(j)
        if cur > mx:
            mx, cnt = cur, 1
        elif cur == mx:
            cnt += 1
        score[i] = cur
    # print(score)
    idx = sorted(range(m), key = lambda x: -vals[x])

    for i in range(n):
        if score[i] == mx:
            print(1 if cnt > 1 else 0)
        else:
            ans = 0
            for j in idx:
                if j in unsol[i]:
                    score[i] += vals[j]
                    ans += 1
                    if score[i] > mx:
                        break
            print(ans)

solve()