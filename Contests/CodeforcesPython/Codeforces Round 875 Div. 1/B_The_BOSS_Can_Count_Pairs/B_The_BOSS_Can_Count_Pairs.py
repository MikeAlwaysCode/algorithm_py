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
    B = ints()

    ans = 0
    # cnt = [[0] * (n + 1) for _ in range(n + 1)]
    exist = [False] * (n + 1)
    cnt = [Counter() for _ in range(n + 1)]
    for a, b in zip(A, B):
        cnt[a][b] += 1
        exist[a] = True
        
    A = sorted(set(A))
    
    # for i, a in enumerate(A):
    for i in range(1, n + 1):
        if not exist[i]: continue

        # 相同a之中不同的b
        s = i * i
        for j in cnt[i].keys():
            if j * 2 == s:
                ans += cnt[i][j] * (cnt[i][j] - 1) // 2
            elif j * 2 < s and s - j in cnt[i]:
                ans += cnt[i][j] * cnt[i][s - j]
        
        for j in range(i + 1, n + 1):
            if i * j > n * 2: break
            if not exist[j]: continue

            # AC还是TLE的核心，枚举b元素少的a，判断另一端
            s, u, v = i * j, i, j
            if len(cnt[i]) > len(cnt[j]):
                u, v = v, u
            cu, cv = cnt[u], cnt[v]
            for k in cu.keys():
                if s - k in cv:
                    ans += cu[k] * cv[s - k]
                    
    print(ans)

for _ in range(int(input())):
    solve()