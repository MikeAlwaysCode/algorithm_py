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

    n, m = len(s), len(t)

    dp = [[[-1] * (n + m + 1) for _ in range(m + 1)] for _ in range(n + 1)]
    s += "!"
    t += "!"
    q = deque([0])
    mask = (1 << 10) - 1
    while q:
        tmp = []
        for u in q:
            i, j, k = u >> 20, (u >> 10) & mask, u & mask
            x, y, z = i + int(s[i] == "("), j + int(t[j] == "("), k + 1
            if z <= m + n and -1 == dp[x][y][z]:
                dp[x][y][z] = u
                tmp.append((x << 20 | y << 10 | z))
            x, y, z = i + int(s[i] == ")"), j + int(t[j] == ")"), k - 1
            if z >= 0 and -1 == dp[x][y][z]:
                dp[x][y][z] = u
                tmp.append((x << 20 | y << 10 | z))
        q = tmp

    ans = []
    i, j, k = n, m, 0
    while i or j or k:
        u = dp[i][j][k]
        i, j, z = u >> 20, (u >> 10) & mask, u & mask
        if z < k:
            ans.append("(")
        else:
            ans.append(")")
        k = z
    print("".join(ans[::-1]))


    '''
    # 贪心是错误的
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[0] = list(range(m + 1))
    for i in range(1, n + 1):
        dp[i][0] = i
    for i, x in enumerate(s):
        for j, y in enumerate(t):
            if x == y:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = min(dp[i + 1][j], dp[i][j + 1]) + 1
    ans = []
    i, j = n - 1, m - 1
    while i >= 0 and j >= 0:
        if s[i] == t[j]:
            ans.append(s[i])
            i -= 1
            j -= 1
        elif dp[i][j + 1] == dp[i + 1][j]:
            if s[i] == ")":
                ans.append(s[i])
                i -= 1
            else:
                ans.append(t[j])
                j -= 1
        elif dp[i + 1][j + 1] == dp[i][j + 1] + 1:
            ans.append(s[i])
            i -= 1
        else:
            ans.append(t[j])
            j -= 1
    ans.reverse()
    
    ans = list(s[:i + 1]) + list(t[:j + 1]) + ans

    left, right = [], []

    cnt1 = mx = 0
    for c in ans:
        if c == "(":
            cnt1 -= 1
        else:
            cnt1 += 1
        mx = max(mx, cnt1)

    if mx > 0:
        left = ["("] * mx
        cnt1 = mx
    else:
        cnt1 = 0
    
    cnt2 = mx = 0
    for c in ans[::-1]:
        if c == "(":
            cnt2 += 1
        else:
            cnt2 -= 1
        mx = max(mx, cnt2)

    if mx > 0:
        right = [")"] * mx
        cnt2 -= mx

    cnt = cnt2 + cnt1

    if cnt > 0:
        right.extend([")"] * cnt)
    elif cnt < 0:
        left.extend(["("] * abs(cnt))

    ans = left + ans + right

    print("".join(ans))
    '''

# for _ in range(int(input())):
solve()