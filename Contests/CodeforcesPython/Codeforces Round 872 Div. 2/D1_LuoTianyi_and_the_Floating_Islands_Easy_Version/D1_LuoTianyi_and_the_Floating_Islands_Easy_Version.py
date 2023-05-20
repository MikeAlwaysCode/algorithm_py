import math
import sys
from bisect import *
from collections import *
from functools import *
from heapq import *
from itertools import *
from random import *
from string import *

# region fastio
input = lambda: sys.stdin.readline().rstrip()
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998244353
MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def solve() -> None:
    n, k = mint()
    g = [[] for _ in range(n)]
    deg = [0] * n
    for _ in range(n - 1):
        u, v = mint()
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)
        deg[u] += 1
        deg[v] += 1

    if k == 1 or k == 3:
        print(1)
        return
    
    	# 阶乘
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i-1] * i % MOD

    # 逆元
    inverse = [0] * (n + 1)
    inverse[n] = pow(fact[n], MOD - 2, MOD)
    for i in range(n, 0, -1):
        inverse[i-1] = inverse[i] * i % MOD

    # 组合数
    def comb(n: int, m: int, MOD = MOD) -> int:
        if m < 0 or m > n:
            return 0
        return fact[n] * inverse[m] % MOD * inverse[n-m] % MOD

    cnt = [1] * n
    p = 0
    if k == 2:
        dq = deque([i for i in range(n) if deg[i] == 1])
        while dq:
            x = dq.popleft()
            # p = (p + cnt[x] * (n - cnt[x] + 1) - 1) % MOD
            p = (p + n - 1) % MOD
            for y in g[x]:
                if deg[y] <= 1: continue
                p = (p + cnt[x] * (n - cnt[x] - cnt[y])) % MOD
                cnt[y] += cnt[x]
                deg[y] -= 1
                if deg[y] == 1:
                    dq.append(y)
    
    q = comb(n, k)
    ans = p * pow(q, MOD - 2, MOD) % MOD
    print(ans)


# for _ in range(int(input())):
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