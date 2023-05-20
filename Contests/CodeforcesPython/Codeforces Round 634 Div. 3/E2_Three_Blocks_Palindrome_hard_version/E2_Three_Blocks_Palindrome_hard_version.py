import sys
from bisect import *
from collections import *
from functools import *
from heapq import *
from itertools import *
from math import *
from random import *
from string import *

# region fastio
input = lambda: sys.stdin.readline().rstrip()
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998244353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def solve() -> None:
    n = int(input())
    arr = ints()

    # 546 ms
    cnt = [0] * 201
    for a in arr:
        cnt[a] += 1
    ans = max(cnt)
    for k in set(arr):
        tmp = cnt[:]
        i, j = 0, n - 1
        left = right = 0
        for x in range(1, cnt[k] // 2 + 1):
            while left < x:
                if arr[i] == k:
                    left += 1
                tmp[arr[i]] -= 1
                i += 1
            while right < x:
                if arr[j] == k:
                    right += 1
                tmp[arr[j]] -= 1
                j -= 1
            if i > j: break
            ans = max(ans, max(tmp) + x * 2)

    '''
    # 1247 ms
    cnt = Counter(arr)
    ans = cnt.most_common(1)[0][1]
    for k, v in cnt.items():
        tmp = cnt.copy()
        i, j = 0, n - 1
        left = right = 0
        for x in range(1, v // 2 + 1):
            while left < x:
                if arr[i] == k:
                    left += 1
                tmp[arr[i]] -= 1
                i += 1
            while right < x:
                if arr[j] == k:
                    right += 1
                tmp[arr[j]] -= 1
                j -= 1
            if i > j: break
            ans = max(ans, tmp.most_common(1)[0][1] + x * 2)
    '''

    '''
    # MLE
    # pos = [[] for _ in range(201)]
    pos = defaultdict(list)
    # pres = [[0] * 201 for _ in range(n + 1)]
    pres = [Counter() for _ in range(n + 1)]
    for i, a in enumerate(arr):
        pos[a].append(i)
        for j in range(201):
            # pres[i + 1][j] = pres[i][j] + int(j == a)
            if pres[i][j]:
                pres[i + 1][j] = pres[i][j]
            if j == a:
                pres[i + 1][j] += 1
    
    ans = 1
    for i, a in enumerate(arr):
        if pres[i + 1][a] * 2 > pres[-1][a]: continue
        out = pres[i + 1][a]
        r = pos[a][-out]
        # for j in range(201):
        #     ans = max(ans, out * 2 + pres[r][j] - pres[i + 1][j])
        for k, v in pres[r].items():
            ans = max(ans, out * 2 + v - pres[i + 1][k])
    '''
    
    print(ans)

for _ in range(int(input())):
    solve()

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
# from types import GeneratorType
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