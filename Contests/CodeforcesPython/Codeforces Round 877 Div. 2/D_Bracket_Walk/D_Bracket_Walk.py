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
    n, q = mint()
    s = list(input())

    right, right2, left, left2 = [], [], [], []

    for i in range(n):
        if i < n - 1 and s[i] == s[i + 1]:
            if s[i] == "(":
                heappush(right, i)
                heappush(right2, -i)
            else:
                heappush(left, i)
                heappush(left2, -i)
    
    for _ in range(q):
        p = sint()
        p -= 1

        if n & 1:
            print("NO")
            continue

        if s[p] == "(":
            s[p] = ")"
            if p and s[p - 1] == ")":
                heappush(left, p - 1)
                heappush(left2, 1 - p)
            if p < n - 1 and s[p + 1] == ")":
                heappush(left, p)
                heappush(left2, -p)
        else:
            s[p] = "("
            if p and s[p - 1] == "(":
                heappush(right, p - 1)
                heappush(right2, 1 - p)
            if p < n - 1 and s[p + 1] == "(":
                heappush(right, p)
                heappush(right2, -p)

        while right and (s[right[0]] != "(" or s[right[0] + 1] != "("):
            heappop(right)

        while right2 and (s[-right2[0]] != "(" or s[-right2[0] + 1] != "("):
            heappop(right2)

        while left and (s[left[0]] != ")" or s[left[0] + 1] != ")"):
            heappop(left)

        while left2 and (s[-left2[0]] != ")" or s[-left2[0] + 1] != ")"):
            heappop(left2)
        
        if s[0] == ")" or s[-1] == "(":
            print("NO")
        elif not right and not left:
            print("YES")
        elif not right or not left:
            print("NO")
        elif right[0] > left[0] or right2[0] < left2[0]:
            print("NO")
        else:
            print("YES")

# for _ in range(int(input())):
solve()