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
    s = input()
    seg = []
    l = r = 0
    stk = []
    for i, c in enumerate(s):
        if c == "(":
            stk.append(i)
        elif c == ")" and stk:
            l = stk.pop()
            r = i
            while seg and l < seg[-1][0] and r > seg[-1][1]:
                seg.pop()
            
            seg.append((l, r))
    # print(seg)
    if not seg:
        print(s)
    else:
        pre = 0
        ans = ""
        for l, r in seg:
            ans += s[pre:l]
            pre = r + 1
        if pre < n:
            ans += s[pre:]
        print(ans)
    '''
    ans = []
    stk = []
    for c in s:
        if c == "(":
            stk.append(len(ans))
            ans.append(c)
        elif c == ")" and stk:
            ans = ans[:stk.pop()]
        else:
            ans.append(c)
    print("".join(ans))
    '''

solve()