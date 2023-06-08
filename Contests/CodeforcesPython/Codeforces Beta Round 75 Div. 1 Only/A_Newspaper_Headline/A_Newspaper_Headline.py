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
    s = input()
    t = input()

    # 342 ms
    nxt = [[-1] * 26 for _ in range(len(s))]
    pos = [-1] * 26
    for i in range(len(s) - 1, -1, -1):
        pos[ord(s[i]) - 97] = i
    for i in range(len(s) - 1, -1, -1):
        # for j in range(26):
        #     nxt[i][j] = pos[j]
        nxt[i] = pos[:]
        pos[ord(s[i]) - 97] = i
    
    # print(nxt)

    ans, pre = 0, len(s) - 1
    for c in t:
        d = ord(c) - 97
        np = nxt[pre][d]
        if np == -1:
            print(-1)
            return
        if np <= pre:
            ans += 1
        pre = np
    '''
    # 496 ms
    pos = [[] for _ in range(26)]
    for i, c in enumerate(s):
        pos[ord(c) - 97].append(i)

    ans, pre = 0, len(s)
    for c in t:
        d = ord(c) - 97
        if not pos[d]:
            print(-1)
            return
        if pre >= pos[d][-1]:
            ans += 1
            pre = pos[d][0]
        else:
            pre = pos[d][bisect_right(pos[d], pre)]
    '''

    '''
    # 622 ms
    pos = defaultdict(list)
    for i, c in enumerate(s):
        pos[c].append(i)

    ans, pre = 0, len(s)
    for c in t:
        if c not in pos:
            print(-1)
            return
        if pre >= pos[c][-1]:
            ans += 1
            pre = pos[c][0]
        else:
            pre = pos[c][bisect_right(pos[c], pre)]
    '''

    print(ans)

# for _ in range(int(input())):
solve()