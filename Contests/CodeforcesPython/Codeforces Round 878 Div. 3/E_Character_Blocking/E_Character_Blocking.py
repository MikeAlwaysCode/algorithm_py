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
    s = []
    s.append(list(input()))
    s.append(list(input()))
    
    n = len(s[0])

    # 436 ms
    block = Counter()
    diff = 0
    for i in range(n):
        if s[0][i] != s[1][i]: diff += 1

    t, q = mint()
    for i in range(q):
        qry = ints()

        diff += block[i]

        if qry[0] == 1: # block
            pos = qry[1] - 1
            if s[0][pos] != s[1][pos]:
                diff -= 1
                block[i + t] += 1
        elif qry[0] == 2:   # swap
            j, pos1, k, pos2 = qry[1:]
            j -= 1
            k -= 1
            pos1 -= 1
            pos2 -= 1
            
            if s[0][pos1] != s[1][pos1]: diff -= 1
            if s[0][pos2] != s[1][pos2] and pos2 != pos1: diff -= 1

            s[j][pos1], s[k][pos2] = s[k][pos2], s[j][pos1]
            
            if s[0][pos1] != s[1][pos1]: diff += 1
            if s[0][pos2] != s[1][pos2] and pos2 != pos1: diff += 1
        else:           # answer
            print("YES" if not diff else "NO")
    '''
    # 529 ms
    diff = set()
    block = deque()

    for i in range(n):
        if s[0][i] != s[1][i]: diff.add(i)
    
    t, q = mint()
    for i in range(q):
        qry = ints()

        while block and block[0][0] + t <= i:
            pos = block.popleft()[1]
            if s[0][pos] != s[1][pos]: diff.add(pos)

        if qry[0] == 1: # block
            pos = qry[1] - 1
            block.append((i, pos))
            if pos in diff:
                diff.remove(pos)
        elif qry[0] == 2:   # swap
            j, pos1, k, pos2 = qry[1:]
            j -= 1
            k -= 1
            pos1 -= 1
            pos2 -= 1
            s[j][pos1], s[k][pos2] = s[k][pos2], s[j][pos1]
            if s[0][pos1] != s[1][pos1]:
                diff.add(pos1)
            elif pos1 in diff:
                diff.remove(pos1)
            if s[0][pos2] != s[1][pos2]:
                diff.add(pos2)
            elif pos2 in diff:
                diff.remove(pos2)
        else:           # answer
            print("YES" if not diff else "NO")
    '''

for _ in range(int(input())):
    solve()