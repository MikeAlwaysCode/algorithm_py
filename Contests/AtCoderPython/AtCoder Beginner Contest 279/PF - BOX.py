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
    n, q = mint()

    box = list(range(n + 1))
    ball = list(range(n + 1))
    fa = list(range(n + 1))
    def find(x: int) -> int:
        cur = x
        while x != fa[x]:
            x = fa[x]
        while fa[cur] != x:
            fa[cur], cur = x, fa[cur]
        return x
    
    for _ in range(q):
        qry = ints()
        if qry[0] == 1:
            x, y = box[qry[1]], box[qry[2]]
            if y == -1:
                continue
            if x == -1:
                box[qry[1]] = y
                ball[y] = qry[1]
            else:
                fa[y] = x
            box[qry[2]] = -1
        elif qry[0] == 2:
            n += 1
            fa.append(n)
            ball.append(n)
            x = box[qry[1]]
            if x == -1:
                ball[-1] = qry[1]
                box[qry[1]] = n
            else:
                fa[-1] = x
        else:
            print(ball[find(qry[1])])

solve()