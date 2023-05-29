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
    s = list(map(int, list(input())))

    cnt = Counter(s)
    
    m = n // 3
    less = deque([i for i in range(3) if cnt[i] < m])

    i, j = 0, n - 1
    while less:
        while i < n and cnt[s[i]] <= m:
            i += 1
        while j >= 0 and cnt[s[j]] <= m:
            j -= 1
        if i < n and s[i] > less[0]:
            cnt[s[i]] -= 1
            s[i] = less[0]
            cnt[less[0]] += 1
            if cnt[less[0]] == m: less.popleft()
            i += 1
        elif j >= 0 and s[j] < less[-1]:
            cnt[s[j]] -= 1
            s[j] = less[-1]
            cnt[less[-1]] += 1
            if cnt[less[-1]] == m: less.pop()
            j -= 1
        else:
            i += 1
            j -= 1

    print(*s, sep = "")


# for _ in range(int(input())):
solve()